import requests
import subprocess
import time
def set_reminder(title, message, seconds_delay):
    applescript = f'do shell script "sleep {seconds_delay} && osascript -e \'display notification \\"{message}\\" with title \\"{title}\\" sound name \\"Glass\\"\'"'
    subprocess.run(["osascript", "-e", applescript])
delaytime=1
def main():
    global delaytime
    try:
        response = requests.get("https://codeforces.com/api/contest.list?gym=false")
        obj = response.json()
        next_contest = {}
        for contest in obj["result"]:
            if contest["phase"] == "BEFORE":
                time = -1 * contest["relativeTimeSeconds"]
                name = contest["name"]
                if not next_contest:  # Check if next_contest is empty
                    next_contest.update({name: time})
                else:
                    if time < next_contest[next(iter(next_contest))]:
                        next_contest = {name: time} # Update next_contest with the new contest
            
            #now we have the nearest upcoming contest in the next_contest
        
        value=next_contest[next(iter(next_contest))]
        delaytime = value/2
        #print(value)               
        if time<300:
            set_reminder(name,f"will start in less than {value} minutes",0)

    except requests.exceptions.RequestException as err:
        delaytime=3600
        
if __name__ == "__main__":
    while True:
        main()
        #print(delaytime)
        time.sleep(delaytime)


#set_reminder(contest["name"],"contest will start soon",-1*contest["relativeTimeSeconds"])
#print(f'{name} {time//3600}:{(time%3600)//60}:{(time%3600)%60}')
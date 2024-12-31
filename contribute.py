import os
import random
import subprocess
import datetime

def generate_contributions(repo_path, days, max_commits, skip_weekends):
    os.chdir(repo_path)
    today = datetime.date.today()

    for day in range(days):
        date = today - datetime.timedelta(days=day)
        if skip_weekends and date.weekday() >= 5:
            continue

        num_commits = random.randint(1, max_commits)
        for _ in range(num_commits):
            with open("README.md", "a") as f:
                f.write(f"Commit on {date}\n")
            subprocess.run(["git", "add", "README.md"])
            subprocess.run(["git", "commit", "--date", str(date), "-m", f"Commit on {date}"])

if __name__ == "__main__":
    repo_path = input("Enter the path to your local repository: ").strip()
    days = int(input("Enter the number of days: ").strip())
    max_commits = int(input("Enter the maximum number of commits per day: ").strip())
    skip_weekends = input("Skip weekends? (yes/no): ").strip().lower() == "yes"

    generate_contributions(repo_path, days, max_commits, skip_weekends)

import subprocess
import schedule
import time
import threading
from datetime import datetime

def auto_commit():
    try:
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=".")
        if result.stdout.strip():
            subprocess.run(["git", "add", "data/"], cwd=".")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            subprocess.run(["git", "commit", "-m", f"Auto-commit: Dataset progress at {timestamp}"], cwd=".")
            print(f"Auto-committed at {timestamp}")
        else:
            print("No changes to commit")
    except Exception as e:
        print(f"Auto-commit error: {e}")

def start_scheduler(interval_minutes=15):
    schedule.every(interval_minutes).minutes.do(auto_commit)
    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(1)
    thread = threading.Thread(target=run_scheduler, daemon=True)
    thread.start()
    return thread

def stop_scheduler():
    schedule.clear()
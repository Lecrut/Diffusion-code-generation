if __name__ == '__main__':
    hours = 3
    minutes = 45
    seconds = 30
    total_minutes = (hours * 60) + minutes + (seconds / 60.0)
    print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")
    print(f"Total minutes: {total_minutes}")
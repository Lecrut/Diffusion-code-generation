from datetime import datetime

def time_difference(start_time, end_time):
    start = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    delta = end - start
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours} hours, {minutes} minutes, and {seconds} seconds"

if __name__ == '__main__':
    print(time_difference("2023-10-01 12:00:00", "2023-10-01 15:30:45"))
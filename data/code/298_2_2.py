from datetime import datetime

def time_difference(time1: str, time2: str) -> tuple:
    format_str = "%H:%M:%S"
    tdelta = datetime.strptime(time2, format_str) - datetime.strptime(time1, format_str)
    hours, remainder = divmod(tdelta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds

if __name__ == '__main__':
    print(time_difference("12:00:00", "14:30:45"))
from datetime import datetime

def time_difference(time1: str, time2: str) -> str:
    format_str = "%H:%M"
    tdelta = abs(datetime.strptime(time2, format_str) - datetime.strptime(time1, format_str))
    hours, remainder = divmod(tdelta.seconds, 3600)
    minutes = remainder // 60
    return f"{hours} hour{'s' if hours != 1 else ''}, {minutes} minute{'s' if minutes != 1 else ''}"

if __name__ == '__main__':
    print(time_difference("14:30", "20:45"))
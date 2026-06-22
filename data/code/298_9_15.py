from datetime import datetime

def time_difference(time1: str, time2: str) -> int:
    format_str = "%H:%M"
    tdelta = datetime.strptime(time2, format_str) - datetime.strptime(time1, format_str)
    return abs(tdelta.total_seconds() / 60)

if __name__ == '__main__':
    print(time_difference('09:45', '23:15'))
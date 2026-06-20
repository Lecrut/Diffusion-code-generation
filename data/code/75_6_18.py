from datetime import datetime

def time_difference(date1: str, date2: str) -> tuple:
    format_str = "%Y-%m-%d %H:%M:%S"
    a = datetime.strptime(date1, format_str)
    b = datetime.strptime(date2, format_str)
    delta = abs(b - a)
    hours, remainder = divmod(delta.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    return int(hours), int(minutes), int(seconds)

if __name__ == '__main__':
    print(time_difference("2023-10-01 12:00:00", "2023-10-01 14:30:45"))
from datetime import datetime

def time_difference_ms(time1: str, time2: str) -> int:
    format_str = '%H:%M:%S'
    tdelta = datetime.strptime(time2, format_str) - datetime.strptime(time1, format_str)
    return abs(tdelta.total_seconds() * 1000)

if __name__ == '__main__':
    print(time_difference_ms('12:34:56', '12:35:57'))
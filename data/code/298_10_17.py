from datetime import datetime

def calculate_time_difference(time_str1: str, time_str2: str) -> int:
    try:
        time_format = '%H:%M'
        time1 = datetime.strptime(time_str1, time_format)
        time2 = datetime.strptime(time_str2, time_format)
        difference = abs((time2 - time1).seconds // 60)
        return difference
    except ValueError:
        return None

if __name__ == '__main__':
    time_a = "01:00"
    time_b = "03:45"
    result = calculate_time_difference(time_a, time_b)
    print(result)
from datetime import datetime

def calculate_time_difference(time_str1: str, time_str2: str) -> int:
    try:
        format_str = '%H:%M'
        dt1 = datetime.strptime(time_str1, format_str)
        dt2 = datetime.strptime(time_str2, format_str)
        time_diff_minutes = (dt2 - dt1).seconds // 60
        return abs(time_diff_minutes)
    except ValueError:
        raise ValueError("Invalid time format. Please use 'HH:MM'.")
if __name__ == '__main__':
    time_a = '09:30'
    time_b = '14:45'
    try:
        difference = calculate_time_difference(time_a, time_b)
        print(f'Time Difference in Minutes: {difference}')
    except ValueError as e:
        print(e)
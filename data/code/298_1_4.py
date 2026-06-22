from datetime import datetime

def time_difference_seconds(time1_str, time2_str):
    format_str = "%H:%M"
    try:
        time1 = datetime.strptime(time1_str, format_str)
        time2 = datetime.strptime(time2_str, format_str)
        tdelta = abs(time2 - time1)
        return tdelta.total_seconds()
    except ValueError:
        raise ValueError("Invalid time format. Please use HH:MM.")

if __name__ == '__main__':
    print(int(time_difference_seconds('14:30', '16:45')))
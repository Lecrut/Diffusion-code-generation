from datetime import datetime

def calculate_duration(start_time_str, end_time_str):
    try:
        start_time = datetime.strptime(start_time_str, '%H:%M')
        end_time = datetime.strptime(end_time_str, '%H:%M')
        if start_time > end_time:
            end_time += timedelta(days=1)
        duration = (end_time - start_time).seconds
        return duration
    except ValueError:
        print("Invalid time format. Please use 'HH:MM'")
        return None

if __name__ == '__main__':
    print(calculate_duration('11:30', '14:15'))
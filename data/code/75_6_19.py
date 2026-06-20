from datetime import datetime

def time_difference(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S")
    delta = end_date - start_date
    total_seconds = delta.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

if __name__ == '__main__':
    print(time_difference("2023-10-01 12:00:00", "2023-10-01 14:30:45"))
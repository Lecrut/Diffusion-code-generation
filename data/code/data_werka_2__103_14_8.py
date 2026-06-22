import datetime
def compute_time_since_midnight(reference_hour, reference_minute, reference_second):
    base_date = datetime.date.today()
    current_time = datetime.time(reference_hour, reference_minute, reference_second)
    start_of_day = datetime.time(0, 0, 0)
    current_datetime = datetime.datetime.combine(base_date, current_time)
    start_datetime = datetime.datetime.combine(base_date, start_of_day)
    duration = current_datetime - start_datetime
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
if __name__ == '__main__':
    result = compute_time_since_midnight(10, 30, 45)
    print(result)
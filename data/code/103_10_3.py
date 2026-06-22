import datetime

def calculate_elapsed_time_since_start_of_day(target_date):
    start_of_day = datetime.datetime.combine(target_date, datetime.time.min)
    end_of_day = datetime.datetime.combine(target_date, datetime.time.max)
    total_seconds_in_day = (end_of_day - start_of_day).total_seconds()
    current_time = datetime.datetime.now()
    if current_time.date() != target_date:
        raise ValueError("Current date does not match target date")
    elapsed_seconds = (current_time - start_of_day).total_seconds()
    return elapsed_seconds

if __name__ == '__main__':
    today = datetime.date.today()
    result = calculate_elapsed_time_since_start_of_day(today)
    print(result)
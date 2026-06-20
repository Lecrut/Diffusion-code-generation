import datetime

def find_next_day_of_week(start_date, target_day):
    if not isinstance(start_date, datetime.date) or not isinstance(target_day, str):
        raise ValueError("Invalid input types. start_date must be a date object and target_day must be a string.")
    
    target_day = target_day.lower()
    days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    if target_day not in days_of_week:
        raise ValueError("Invalid day of the week. Must be one of 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', or 'Sunday'.")
    
    start_day_index = days_of_week.index(start_date.strftime("%A").lower())
    target_day_index = days_of_week.index(target_day)
    
    days_until_target = (target_day_index - start_day_index) % 7
    next_target_date = start_date + datetime.timedelta(days=days_until_target)
    
    return next_target_date

if __name__ == '__main__':
    sample_start_date = datetime.date(2023, 9, 15)
    target_day = "thursday"
    try:
        result_date = find_next_day_of_week(sample_start_date, target_day)
        print(result_date.strftime("%Y-%m-%d"))
    except ValueError as e:
        print(e)
def is_weekend_or_holiday(date):
    weekdays = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}
    holidays = {'2023-10-12'}
    
    day_of_week = date.split('-')[2]
    if day_of_week in weekdays:
        return "Weekend"
    elif date in holidays:
        return "Holiday"
    else:
        return "Workday"

if __name__ == '__main__':
    print(is_weekend_or_holiday('2023-10-12'))
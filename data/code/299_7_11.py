def is_weekend_or_holiday(date):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    holidays = ['2023-10-12']
    
    if date in holidays:
        return True
    
    from datetime import datetime
    day_of_week = datetime.strptime(date, '%Y-%m-%d').strftime('%A')
    return day_of_week not in weekdays

if __name__ == '__main__':
    print(is_weekend_or_holiday('2023-10-12'))
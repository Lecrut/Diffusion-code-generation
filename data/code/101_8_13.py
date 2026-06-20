import calendar

def is_valid_date(year, month, day):
    try:
        calendar.weekday(year, month, day)
        return True
    except ValueError:
        return False

def determine_weekday(year, month, day):
    if not is_valid_date(year, month, day):
        raise ValueError("Invalid date")
    
    weekday_num = calendar.weekday(year, month, day)
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[weekday_num]

if __name__ == '__main__':
    print(determine_weekday(2023, 10, 26))
    print(determine_weekday(2023, 10, 27))
    print(determine_weekday(2023, 1, 1))
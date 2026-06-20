import calendar

def is_weekday(year, month, day):
    return calendar.weekday(year, month, day) < 5

if __name__ == '__main__':
    dates = {
        (2023, 10, 23): "Is weekday?",
        (2023, 10, 24): "Is weekday?",
        (2023, 10, 28): "Is not a weekday?",
        (2023, 10, 29): "Is not a weekday?"
    }
    
    for date, message in dates.items():
        print(f"{message} {date[0]}/{date[1]}/{date[2]}: {is_weekday(*date)}")
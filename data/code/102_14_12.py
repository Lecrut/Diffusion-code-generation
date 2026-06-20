import calendar

def is_weekday(date_string):
    try:
        year, month, day = map(int, date_string.split('/'))
        return 0 <= calendar.weekday(year, month, day) <= 4
    except ValueError:
        raise ValueError("Invalid date format or value")

if __name__ == '__main__':
    dates = [
        "01/01/2024",
        "02/29/2024",
        "03/15/2024",
        "12/31/2023",
        "04/30/2024",
        "13/01/2024"
    ]
    
    for date in dates:
        try:
            print(f"Is {date} a weekday? {is_weekday(date)}")
        except ValueError as e:
            print(e)
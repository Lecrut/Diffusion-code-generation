import calendar

def get_day_of_month(year, month, day):
    try:
        _, num_days = calendar.monthrange(year, month)
        if 1 <= day <= num_days:
            return day
        else:
            raise ValueError(f"Day {day} is out of range for the given month and year.")
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_dates = [
        (2023, 10, 5),
        (2022, 12, 25),
        (2024, 2, 29),
        (2023, 4, 30),
        (2023, 7, 32)
    ]
    
    for year, month, day in sample_dates:
        result = get_day_of_month(year, month, day)
        print(f"Year: {year}, Month: {month}, Day: {day} -> {result}")
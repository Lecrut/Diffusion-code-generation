import calendar

def determine_weekday(year, month, day):
    try:
        date_obj = calendar.date.fromisoformat(f"{year}-{month:02d}-{day:02d}")
        return date_obj.strftime("%A")
    except ValueError as e:
        raise ValueError("Invalid date format or out of range") from e

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 26
    print(determine_weekday(sample_year, sample_month, sample_day))
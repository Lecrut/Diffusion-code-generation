import datetime

def calculate_weeks_between_julian_dates(julian_date1, julian_date2):
    try:
        date1 = datetime.datetime.strptime(julian_date1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(julian_date2, '%Y-%m-%d')
        difference = abs(date1 - date2)
        weeks = difference.days / 7
        return weeks
    except ValueError:
        return None

if __name__ == '__main__':
    sample_julian_date1 = "2023-01-15"
    sample_julian_date2 = "2023-03-20"
    result = calculate_weeks_between_julian_dates(sample_julian_date1, sample_julian_date2)
    if result is not None:
        print(f"Julian Date 1: {sample_julian_date1}")
        print(f"Julian Date 2: {sample_julian_date2}")
        print(f"Difference in weeks: {result:.2f}")
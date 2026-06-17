import datetime
def calculate_day_number(year, month, day):
    try:
        date = datetime.date(year, month, day)
        return date.timetuple().tm_yday
    except ValueError:
        return None
if __name__ == '__main__':
    sample_year = 2023
    sample_month = 10
    sample_day = 27
    result = calculate_day_number(sample_year, sample_month, sample_day)
    if result is not None:
        print(result)
    else:
        print("Invalid date provided.")
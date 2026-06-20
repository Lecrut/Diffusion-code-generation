import datetime

def calculate_day_of_year(year, month, day):
    try:
        date_obj = datetime.date(year, month, day)
        return date_obj.timetuple().tm_yday
    except ValueError:
        return None

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 11
    sample_day = 15
    day_of_year = calculate_day_of_year(sample_year, sample_month, sample_day)
    if day_of_year is not None:
        print(f"The day of the year for {sample_year}-{sample_month}-{sample_day} is: {day_of_year}")
    else:
        print("Invalid date entered.")
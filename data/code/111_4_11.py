import datetime

def calculate_seconds_in_year(year):
    try:
        start_date = datetime.date(year, 1, 1)
        end_date = datetime.date(year + 1, 1, 1)
        delta = end_date - start_date
        return delta.total_seconds()
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_year = 2023
    seconds_in_year = calculate_seconds_in_year(sample_year)
    if seconds_in_year is not None:
        print(f"The total number of seconds in the year {sample_year} is: {int(seconds_in_year)}")
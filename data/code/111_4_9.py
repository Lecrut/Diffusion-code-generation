import datetime

def calculate_seconds_in_year(year):
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year + 1, 1, 1)
    delta = end_date - start_date
    return delta.total_seconds()

if __name__ == '__main__':
    year = 2023
    print(calculate_seconds_in_year(year))
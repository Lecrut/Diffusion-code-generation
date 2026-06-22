import datetime

def calculate_seconds_in_year(year):
    start = datetime.date(year, 1, 1)
    end = datetime.date(year + 1, 1, 1)
    delta = end - start
    return delta.days * 24 * 60 * 60

if __name__ == '__main__':
    year = 2023
    total_seconds = calculate_seconds_in_year(year)
    print(total_seconds)
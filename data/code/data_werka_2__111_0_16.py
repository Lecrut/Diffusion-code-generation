from datetime import date

DAYS_IN_NON_LEAP_YEAR = 365
START_YEAR = 2023
START_MONTH = 1
START_DAY = 1
END_MONTH = 12
END_DAY = 31

def compute_days_in_year(year):
    start_date = date(year, START_MONTH, START_DAY)
    end_date = date(year, END_MONTH, END_DAY)
    return (end_date - start_date).days

if __name__ == '__main__':
    target = START_YEAR
    result = compute_days_in_year(target)
    print(result)
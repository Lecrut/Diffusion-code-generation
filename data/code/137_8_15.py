LEAP_YEAR_THRESHOLD = 4
NO_LEAP_YEAR_EXCEPTION = 100
EXCEPTION_DIVISIBILITY = 400

def is_leap_year(year):
    if year % LEAP_YEAR_THRESHOLD == 0:
        if year % NO_LEAP_YEAR_EXCEPTION == 0:
            return year % EXCEPTION_DIVISIBILITY == 0
        return True
    return False

if __name__ == '__main__':
    sample_years = [2000, 1900, 2020, 2021]
    results = {year: is_leap_year(year) for year in sample_years}
    print(results)
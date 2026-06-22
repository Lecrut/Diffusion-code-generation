from datetime import date

def get_days_in_year(year):
    start = date(year, 1, 1)
    end = date(year, 12, 31)
    delta = end - start
    return delta.days

if __name__ == '__main__':
    target_year = 2023
    days_count = get_days_in_year(target_year)
    print(days_count)
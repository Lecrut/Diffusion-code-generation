from datetime import date

def is_valid_date(year, month, day):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

def years_difference(date1, date2):
    if not (is_valid_date(*date1) and is_valid_date(*date2)):
        raise ValueError("Invalid date format")
    return abs((date(*date2) - date(*date1)).days // 365)

if __name__ == '__main__':
    sample_dates = [(2020, 1, 1), (2023, 4, 1)]
    result = years_difference(sample_dates[0], sample_dates[1])
    print(result)
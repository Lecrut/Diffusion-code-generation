from datetime import date, timedelta

def get_next_month(year, month):
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    return date(next_year, next_month)
if __name__ == '__main__':
    result = get_next_month(2023, 11)
    print(result)
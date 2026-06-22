from datetime import date

def days_between(start_date, end_date):
    delta = end_date - start_date
    return delta.days

if __name__ == '__main__':
    start = date(2023, 1, 1)
    end = date(2023, 12, 31)
    result = days_between(start, end)
    print(result)
from datetime import date

def years_between(start: date, end: date) -> int:
    years = end.year - start.year
    if (end.month, end.day) < (start.month, start.day):
        years -= 1
    return years

if __name__ == '__main__':
    start_date = date(2000, 1, 1)
    end_date = date(2023, 12, 31)
    result = years_between(start_date, end_date)
    print(result)
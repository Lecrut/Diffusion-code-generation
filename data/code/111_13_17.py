from datetime import date, timedelta

def add_months(d, months):
    month = d.month - 1 + months
    year = d.year + month // 12
    month = month % 12 + 1
    day = min(d.day, [31, 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
    return date(year, month, day)

if __name__ == '__main__':
    sample_date = date(2023, 4, 30)
    months_to_add = 2
    result_date = add_months(sample_date, months_to_add)
    print(result_date)
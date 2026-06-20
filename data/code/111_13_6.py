from datetime import date, timedelta

def add_months_to_date(base_date, months):
    year = base_date.year + (base_date.month - 1) // 12 + months // 12
    month = ((base_date.month - 1) % 12 + months) % 12 + 1
    day = min(base_date.day, [31, 28 + (year % 4 == 0 and year % 100 != 0 or year % 400 == 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
    return date(year, month, day)

if __name__ == '__main__':
    sample_date = date(2023, 12, 20)
    months_to_add = 5
    result_date = add_months_to_date(sample_date, months_to_add)
    print(result_date)
from datetime import date, timedelta

def add_months_to_date(input_date, months):
    year = input_date.year + (input_date.month - 1 + months) // 12
    month = (input_date.month - 1 + months) % 12 + 1
    day = min(input_date.day, [31, 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
    return date(year, month, day)

if __name__ == '__main__':
    sample_date = date(2023, 4, 30)
    months_to_add = 5
    result_date = add_months_to_date(sample_date, months_to_add)
    print(result_date)
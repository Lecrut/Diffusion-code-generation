def add_months_to_date(date_obj, months):
    year = date_obj.year + (date_obj.month - 1) // 12 + months // 12
    month = ((date_obj.month - 1) % 12 + months) % 12 + 1
    day = min(date_obj.day, [31, 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
    return datetime.date(year, month, day)

if __name__ == '__main__':
    sample_date = "2023-12-15"
    date_obj = datetime.datetime.strptime(sample_date, '%Y-%m-%d').date()
    future_date = add_months_to_date(date_obj, 3)
    print(future_date)
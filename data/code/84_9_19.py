def calculate_day_of_year(date):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (date.year % 4 == 0 and date.year % 100 != 0) or (date.year % 400 == 0):
        month_days[1] = 29
    return sum(month_days[:date.month - 1]) + date.day

if __name__ == '__main__':
    from datetime import date
    sample_date = date(2023, 4, 15)
    print(calculate_day_of_year(sample_date))
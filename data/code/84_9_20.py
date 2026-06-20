def calculate_day_of_year(date_obj):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (date_obj.year % 4 == 0 and date_obj.year % 100 != 0) or date_obj.year % 400 == 0:
        days_in_month[2] = 29
    day_of_year = sum(days_in_month[:date_obj.month]) + date_obj.day
    return day_of_year

if __name__ == '__main__':
    sample_date = (3, 15)
    result1 = calculate_day_of_year(date(sample_date[0], sample_date[1], 1))
    print(f"Month: {sample_date[0]}, Day: {sample_date[1]} -> Day of Year: {result1}")
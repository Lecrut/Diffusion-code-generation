import datetime
def calculate_date_difference(day, month, year):
    current_year = year
    if month == 12:
        end_of_month = datetime.datetime(year, 12, 31)
    else:
        next_month = month + 1
        if next_month > 12:
            next_month = 1
            current_year += 1
        end_of_month = datetime.datetime(year, next_month, 1) - datetime.timedelta(days=1)
    day_of_end = end_of_month.day
    difference = day_of_end - day
    return difference
if __name__ == '__main__':
    sample_day = 25
    sample_month = 10
    sample_year = 2023
    result = calculate_date_difference(sample_day, sample_month, sample_year)
    print(result)
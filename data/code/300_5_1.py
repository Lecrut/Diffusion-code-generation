import datetime
def calculate_month_end_difference(day, month, year):
    current_year = year
    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    end_of_month = datetime.date(next_year, next_month, 1) - datetime.timedelta(days=1)
    day_of_month = datetime.date(current_year, month, day)
    difference = (datetime.date(next_year, next_month, 1) - day_of_month).days
    return difference
if __name__ == '__main__':
    sample_day = 25
    sample_month = 10
    sample_year = 2023
    result = calculate_month_end_difference(sample_day, sample_month, sample_year)
    print(result)
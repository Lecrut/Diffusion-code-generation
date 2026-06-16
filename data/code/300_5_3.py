import datetime
def calculate_date_difference(day, month, year):
    current_year = year
    if month == 12:
        end_of_month = datetime.datetime(year + 1, 1, 1)
    else:
        end_of_month = datetime.datetime(year, month + 1, 1)
    day_of_month = datetime.date(current_year, month, day)
    end_of_month_date = datetime.date(end_of_month.year, end_of_month.month, 1)
    difference = (datetime.date(end_of_month.year, end_of_month.month, 1) - day_of_month).days
    return difference
if __name__ == '__main__':
    sample_day = 25
    sample_month = 10
    sample_year = 2023
    result = calculate_date_difference(sample_day, sample_month, sample_year)
    print(result)
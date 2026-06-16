import calendar
def calculate_date_difference(day, month, year):
    _, num_days = calendar.monthrange(year, month)
    difference = num_days - day
    return difference
if __name__ == '__main__':
    sample_day = 15
    sample_month = 3
    sample_year = 2023
    result = calculate_date_difference(sample_day, sample_month, sample_year)
    print(result)
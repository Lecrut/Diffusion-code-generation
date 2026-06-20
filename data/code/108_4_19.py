import calendar

def get_day_of_month(year, month, day):
    _, num_days = calendar.monthrange(year, month)
    return num_days

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 11
    sample_day = 5
    result = get_day_of_month(sample_year, sample_month, sample_day)
    print(f"Day {sample_day} of Month {sample_month} in the year {sample_year} is valid.")
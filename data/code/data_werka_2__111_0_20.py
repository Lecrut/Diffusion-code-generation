from datetime import date

START_YEAR = 2023
START_MONTH = 1
START_DAY = 1
END_MONTH = 12
END_DAY = 31

def compute_days_in_year(year, start_month, start_day, end_month, end_day):
    start_date = date(year, start_month, start_day)
    end_date = date(year, end_month, end_day)
    delta = end_date - start_date
    return delta.days

if __name__ == '__main__':
    days = compute_days_in_year(START_YEAR, START_MONTH, START_DAY, END_MONTH, END_DAY)
    print(days)
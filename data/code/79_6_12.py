from datetime import date, timedelta

def next_month_date(year, month):
    if month == 12:
        return (year + 1, 1)
    else:
        return (year, month + 1)

if __name__ == '__main__':
    sample_year = 2023
    sample_month = 11
    next_month = next_month_date(sample_year, sample_month)
    print(next_month)
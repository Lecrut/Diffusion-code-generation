import datetime

def days_remaining_in_month(current_year, current_month):
    last_day_of_current_month = datetime.date(current_year, current_month, 1) + datetime.timedelta(days=32)
    return (last_day_of_current_month - datetime.date(current_year, current_month, 1)).days

if __name__ == '__main__':
    sample_year = 2024
    sample_month = 10
    remaining_days = days_remaining_in_month(sample_year, sample_month)
    print(remaining_days)
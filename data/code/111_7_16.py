from datetime import date, timedelta

def add_one_year_and_day(start_date):
    end_date = start_date + timedelta(days=365)
    if start_date.month == 2 and start_date.day == 29 or start_date.day > 31:
        end_date += timedelta(days=1)
    return end_date + timedelta(days=1)
if __name__ == '__main__':
    sample_date = date(2020, 12, 31)
    result_date = add_one_year_and_day(sample_date)
    print(result_date)
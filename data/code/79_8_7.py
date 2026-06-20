import datetime

def get_first_day_next_month(date_obj):
    if date_obj.month == 12:
        return date_obj.replace(year=date_obj.year + 1, month=1)
    else:
        return date_obj.replace(month=date_obj.month + 1)

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    next_month_first_day = get_first_day_next_month(sample_date)
    print(f"Original Date: {sample_date}")
    print(f"First Day of Next Month: {next_month_first_day}")

    sample_date_dec = datetime.date(2023, 12, 31)
    next_month_first_day_dec = get_first_day_next_month(sample_date_dec)
    print(f"Original Date: {sample_date_dec}")
    print(f"First Day of Next Month: {next_month_first_day_dec}")

    sample_date_jan = datetime.date(2024, 1, 5)
    next_month_first_day_jan = get_first_day_next_month(sample_date_jan)
    print(f"Original Date: {sample_date_jan}")
    print(f"First Day of Next Month: {next_month_first_day_jan}")
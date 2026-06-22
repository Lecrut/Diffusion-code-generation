import datetime

def get_seconds_left_in_current_month(reference_date):
    first_day_of_next_month = reference_date.replace(day=1)
    if first_day_of_next_month.month == 12:
        first_day_of_next_month = first_day_of_next_month.replace(year=first_day_of_next_month.year + 1, month=1)
    else:
        first_day_of_next_month = first_day_of_next_month.replace(month=first_day_of_next_month.month + 1)
    time_difference = first_day_of_next_month - reference_date
    total_seconds = int(time_difference.total_seconds())
    return total_seconds

if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 15, 14, 30, 45)
    remaining = get_seconds_left_in_current_month(sample_date)
    print(remaining)
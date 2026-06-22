from datetime import date

def is_weekend_in_range(start_date: date, end_date: date) -> bool:
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() >= 5:
            return True
        current_date += timedelta(days=1)
    return False
if __name__ == '__main__':
    sample_start_date = date(2023, 10, 1)
    sample_end_date = date(2023, 10, 7)
    print(is_weekend_in_range(sample_start_date, sample_end_date))
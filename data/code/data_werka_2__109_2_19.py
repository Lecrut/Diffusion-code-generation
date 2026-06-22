import datetime

START_DATE = datetime.date(2023, 1, 1)
END_DATE = datetime.date(2023, 12, 31)

def get_remaining_time_in_month(reference_date: datetime.date) -> datetime.timedelta:
    if reference_date.month == 12:
        next_month_start = datetime.date(reference_date.year + 1, 1, 1)
    else:
        next_month_start = datetime.date(reference_date.year, reference_date.month + 1, 1)
    
    days_in_month = (next_month_start - reference_date).days
    if days_in_month <= 0:
        raise ValueError("Reference date must be within the month")
    
    return datetime.timedelta(days=days_in_month)

if __name__ == '__main__':
    sample_date = datetime.date(2023, 1, 15)
    result = get_remaining_time_in_month(sample_date)
    print(result)
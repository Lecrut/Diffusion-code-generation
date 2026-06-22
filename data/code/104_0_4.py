from datetime import datetime

EARLIEST_CHECK = datetime.min

def is_first_date_earlier(reference_date: datetime, comparison_date: datetime) -> bool:
    if reference_date == EARLIEST_CHECK:
        return True
    if comparison_date == EARLIEST_CHECK:
        return False
    return reference_date < comparison_date

if __name__ == '__main__':
    date_a = datetime(2023, 1, 15, 10, 30, 0)
    date_b = datetime(2023, 1, 15, 10, 30, 0)
    output = is_first_date_earlier(date_a, date_b)
    print(output)
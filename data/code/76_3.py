import datetime
def days_elapsed(date1: datetime.date, date2: datetime.date) -> int:
    earlier_date = min(date1, date2)
    later_date = max(date1, date2)
    return (later_date - earlier_date).days
if __name__ == '__main__':
    date_a = datetime.date(2023, 1, 10)
    date_b = datetime.date(2023, 1, 5)
    result1 = days_elapsed(date_a, date_b)
    print(result1)
    date_c = datetime.date(2024, 5, 20)
    date_d = datetime.date(2024, 4, 1)
    result2 = days_elapsed(date_c, date_d)
    print(result2)
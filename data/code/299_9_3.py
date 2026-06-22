from datetime import date

def is_weekend_in_range(start_date, end_date):
    for current_date in range(start_date.toordinal(), end_date.toordinal() + 1):
        if date.fromordinal(current_date).weekday() >= 5:
            return True
    return False

if __name__ == '__main__':
    start = date(2023, 4, 1)
    end = date(2023, 4, 7)
    print(is_weekend_in_range(start, end))
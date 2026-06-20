from datetime import date, timedelta

def is_tuesday(input_date: date) -> bool:
    return input_date.weekday() == 1

def get_next_tuesday(start_date: date) -> date:
    days_until_tuesday = (6 - start_date.weekday()) % 7 + 14
    next_tuesday = start_date + timedelta(days=days_until_tuesday)
    return next_tuesday

if __name__ == '__main__':
    reference_date = date(2023, 7, 4)
    print(get_next_tuesday(reference_date))
from datetime import date, timedelta

def calculate_next_sunday(start: date) -> date:
    if start.weekday() == 6:
        days_to_add = 7
    else:
        days_to_add = 6 - start.weekday()
    return start + timedelta(days=days_to_add)

if __name__ == '__main__':
    start_date = date(2024, 1, 1)
    result = calculate_next_sunday(start_date)
    print(result)
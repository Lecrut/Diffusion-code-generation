from datetime import date, timedelta

def add_days_to_date(base_date: date, days: int) -> str:
    target_date = base_date + timedelta(days=days)
    return target_date.strftime("%Y-%m-%d")

if __name__ == '__main__':
    initial_date = date(2024, 7, 4)
    days_to_add = 30
    formatted_result = add_days_to_date(initial_date, days_to_add)
    print(formatted_result)
from datetime import date, timedelta

def calculate_next_friday(reference_date):
    reference_datetime = date.fromisoformat(reference_date)
    days_until_friday = (4 - reference_datetime.weekday()) % 7
    if days_until_friday == 0:
        days_until_friday = 7
    return (reference_datetime + timedelta(days=days_until_friday)).strftime('%Y-%m-%d')

if __name__ == '__main__':
    sample_date = "2023-12-15"
    next_friday_str = calculate_next_friday(sample_date)
    print(next_friday_str)
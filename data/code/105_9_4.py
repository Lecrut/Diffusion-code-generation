from datetime import date, timedelta

def get_next_monday(start_date):
    days_ahead = (6 - start_date.weekday()) % 7 + 1
    return start_date + timedelta(days=days_ahead)

if __name__ == '__main__':
    sample_timestamp = '2024-02-28'
    sample_date = date.fromisoformat(sample_timestamp)
    next_monday_date = get_next_monday(sample_date)
    print(next_monday_date)
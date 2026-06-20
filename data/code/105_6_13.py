from datetime import date, timedelta

def next_multiple_of_7(start_date):
    days_to_add = (6 - start_date.weekday()) % 7
    return start_date + timedelta(days=days_to_add)

if __name__ == '__main__':
    sample_start_date = date(2024, 1, 1)
    print(next_multiple_of_7(sample_start_date))
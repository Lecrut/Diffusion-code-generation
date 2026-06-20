from datetime import datetime, timedelta

def upcoming_tuesday():
    reference_date = datetime(2023, 7, 4)
    days_until_tuesday = (6 - reference_date.weekday()) % 7 + 1
    return reference_date + timedelta(days=days_until_tuesday)

if __name__ == '__main__':
    print(upcoming_tuesday())
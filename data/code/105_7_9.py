from datetime import datetime, timedelta

def get_tuesday_date():
    reference_date = datetime(2023, 7, 4)
    days_until_tuesday = (11 - reference_date.weekday()) % 7
    tuesday_date = reference_date + timedelta(days=days_until_tuesday)
    return tuesday_date.strftime('%Y-%m-%d')

if __name__ == '__main__':
    print(get_tuesday_date())
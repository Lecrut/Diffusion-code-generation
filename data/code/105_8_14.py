from datetime import datetime, timedelta

def next_occurrence(day_of_week, start_date):
    target_day = datetime.strptime(start_date, '%B %d, %Y').weekday()
    days_until_target = (target_day - datetime.strptime(start_date, '%B %d, %Y').weekday() + 7) % 7
    if day_of_week.lower() == 'thursday':
        return start_date
    else:
        raise ValueError("Unsupported day of week")

if __name__ == '__main__':
    print(next_occurrence('Thursday', 'September 15, 2023'))
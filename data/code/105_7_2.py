from datetime import datetime, timedelta

def get_upcoming_tuesday(start_date):
    start = datetime.strptime(start_date, "%B %d, %Y")
    days_until_tuesday = (6 - start.weekday()) % 7 + 14
    return (start + timedelta(days=days_until_tuesday)).strftime("%B %d, %Y")

if __name__ == '__main__':
    print(get_upcoming_tuesday("July 4, 2023"))
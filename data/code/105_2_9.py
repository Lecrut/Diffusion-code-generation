from datetime import datetime, timedelta

def get_upcoming_friday(reference_date):
    reference = datetime.strptime(reference_date, '%B %d, %Y')
    days_until_friday = (4 - reference.weekday()) % 7
    upcoming_friday = reference + timedelta(days=days_until_friday)
    return upcoming_friday.strftime('%B %d, %Y')

if __name__ == '__main__':
    print(get_upcoming_friday('December 15, 2023'))
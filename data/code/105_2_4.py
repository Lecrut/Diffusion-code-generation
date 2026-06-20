from datetime import datetime, timedelta

def upcoming_friday(reference_date):
    reference = datetime.strptime(reference_date, "%B %d, %Y")
    days_until_friday = (4 - reference.weekday()) % 7
    return (reference + timedelta(days=days_until_friday)).strftime("%B %d, %Y")

if __name__ == '__main__':
    print(upcoming_friday("December 15, 2023"))
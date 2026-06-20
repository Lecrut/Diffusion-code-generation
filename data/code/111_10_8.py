import datetime
REFERENCE_DATE = datetime.date(2023, 10, 1)

def days_since_reference():
    today = datetime.date.today()
    return (today - REFERENCE_DATE).days
if __name__ == '__main__':
    print(f'Days since {REFERENCE_DATE}: {days_since_reference()}')
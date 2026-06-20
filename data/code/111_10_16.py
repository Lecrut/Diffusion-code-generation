from datetime import datetime

DAYS_PER_MONTH = 30
HARD_CODED_DATE1 = datetime(2023, 9, 1)
HARD_CODED_DATE2 = datetime(2023, 10, 15)

def days_difference(date1=HARD_CODED_DATE1, date2=HARD_CODED_DATE2):
    return abs((date2 - date1).days)

if __name__ == '__main__':
    print(f"Days between {HARD_CODED_DATE1.date()} and {HARD_CODED_DATE2.date()}: {days_difference()}")
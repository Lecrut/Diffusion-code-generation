from datetime import datetime, timedelta

TODAY = datetime.now()
MONDAY_INDEX = 0
DAYS_IN_WEEK = 7
OFFSET_MULTIPLIER = -1

def calculate_next_monday(reference: datetime) -> datetime:
    current_weekday = reference.weekday()
    difference = (MONDAY_INDEX - current_weekday) * OFFSET_MULTIPLIER
    adjustment = difference % DAYS_IN_WEEK
    if adjustment == 0:
        adjustment = DAYS_IN_WEEK
    return reference + timedelta(days=adjustment)

if __name__ == '__main__':
    result = calculate_next_monday(TODAY)
    print(result.strftime('%Y-%m-%d'))
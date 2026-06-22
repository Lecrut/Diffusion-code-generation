from datetime import datetime, timedelta

FRIDAY_INDEX = 4
DAYS_IN_WEEK = 7

TARGET_WEEKDAYS = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

REFERENCE_DATE = datetime(2023, 12, 15)

def compute_next_target_weekday(reference_date, target_weekday):
    current_weekday = reference_date.weekday()
    days_until_target = target_weekday - current_weekday
    
    if days_until_target <= 0:
        days_until_target += DAYS_IN_WEEK
    
    next_date = reference_date + timedelta(days=days_until_target)
    return next_date

def get_upcoming_friday(date_obj):
    return compute_next_target_weekday(date_obj, FRIDAY_INDEX)

if __name__ == '__main__':
    ref_date = REFERENCE_DATE
    next_fri = get_upcoming_friday(ref_date)
    formatted_date = next_fri.strftime("%Y-%m-%d")
    print(formatted_date)
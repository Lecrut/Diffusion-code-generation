from datetime import datetime, timedelta

DAY_MAP = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}

TARGET_DAY_NAME = "Friday"
TARGET_DAY_INDEX = DAY_MAP[TARGET_DAY_NAME]

REFERENCE_DATE = datetime(2023, 12, 15)

def calculate_next_weekday(reference, target_index):
    current_index = reference.weekday()
    difference = target_index - current_index
    if difference <= 0:
        difference += 7
    return reference + timedelta(days=difference)

def get_upcoming_friday(date):
    return calculate_next_weekday(date, TARGET_DAY_INDEX)

if __name__ == '__main__':
    result = get_upcoming_friday(REFERENCE_DATE)
    print(result.strftime("%Y-%m-%d"))
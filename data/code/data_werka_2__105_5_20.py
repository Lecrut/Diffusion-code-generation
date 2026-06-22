from datetime import date, timedelta

WEEKDAY_MAP = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
TARGET_DAY = 2

def find_next_weekday_reference(reference: date, target: int = TARGET_DAY) -> date:
    current = reference
    while current.weekday() != target:
        current += timedelta(days=1)
    return current

if __name__ == '__main__':
    ref_date = date(2023, 10, 10)
    computed_date = find_next_weekday_reference(ref_date)
    print(computed_date)
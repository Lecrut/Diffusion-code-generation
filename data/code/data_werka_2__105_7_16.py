from datetime import date, timedelta

def find_next_tuesday(anchor: date) -> date:
    target_weekday = 1
    current_weekday = anchor.weekday()
    days_to_add = (target_weekday - current_weekday) % 7
    if days_to_add == 0:
        days_to_add = 7
    return anchor + timedelta(days=days_to_add)

if __name__ == '__main__':
    ref_date = date(2023, 7, 4)
    result = find_next_tuesday(ref_date)
    print(result)
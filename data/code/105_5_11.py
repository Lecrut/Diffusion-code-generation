from datetime import date, timedelta

WEDNESDAY_INDEX = 2
DAYS_IN_WEEK = 7

def get_next_wednesday_after(target_date: date) -> date:
    current_weekday = target_date.weekday()
    days_to_add = WEDNESDAY_INDEX - current_weekday
    if days_to_add <= 0:
        days_to_add += DAYS_IN_WEEK
    return target_date + timedelta(days=days_to_add)

if __name__ == '__main__':
    base_date = date(2023, 10, 10)
    computed_date = get_next_wednesday_after(base_date)
    print(computed_date)
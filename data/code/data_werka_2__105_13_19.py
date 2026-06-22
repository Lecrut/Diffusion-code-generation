from datetime import date, timedelta
from typing import Optional

WEEKDAY_MONDAY = 0
WEEKDAY_SATURDAY = 5
WEEKDAY_SUNDAY = 6
WEEKEND_DAYS = (WEEKDAY_SATURDAY, WEEKDAY_SUNDAY)
DAYS_IN_WEEK = 7

def find_next_weekend_start() -> date:
    today = date.today()
    current_weekday = today.weekday()
    
    if current_weekday in WEEKEND_DAYS:
        return today
    
    days_until_saturday = WEEKDAY_SATURDAY - current_weekday
    saturday = today + timedelta(days=days_until_saturday)
    
    return saturday

if __name__ == '__main__':
    result_date = find_next_weekend_start()
    print(result_date)
from datetime import date, timedelta
from collections import OrderedDict

WEEKEND_DAYS = OrderedDict([
    (0, "Monday"),
    (1, "Tuesday"),
    (2, "Wednesday"),
    (3, "Thursday"),
    (4, "Friday"),
    (5, "Saturday"),
    (6, "Sunday")
])

def find_immediate_next_weekend_date():
    today = date.today()
    current_weekday = today.weekday()
    
    if current_weekday in (5, 6):
        return today
    
    next_weekday = (current_weekday + 1) % 7
    while next_weekday not in (5, 6):
        next_weekday = (next_weekday + 1) % 7
    
    days_to_add = (next_weekday - current_weekday) % 7
    if days_to_add == 0:
        days_to_add = 7
        
    next_weekend = today + timedelta(days=days_to_add)
    return next_weekend

if __name__ == '__main__':
    result = find_immediate_next_weekend_date()
    print(result)
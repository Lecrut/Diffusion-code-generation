from datetime import date, timedelta

WEDNESDAY_INDEX = 2
WEEK_LENGTH = 7
BASE_DATE = date(2023, 10, 10)

def calculate_next_wednesday(reference_date: date) -> date:
    if not isinstance(reference_date, date):
        raise ValueError("Input must be a date object")
    
    current_weekday = reference_date.weekday()
    days_to_add = (WEDNESDAY_INDEX - current_weekday) % WEEK_LENGTH
    
    if days_to_add == 0:
        days_to_add = WEEK_LENGTH
        
    return reference_date + timedelta(days=days_to_add)

if __name__ == '__main__':
    target = calculate_next_wednesday(BASE_DATE)
    print(target)
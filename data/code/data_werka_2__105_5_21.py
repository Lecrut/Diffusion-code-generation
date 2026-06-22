from datetime import date, timedelta

WEDNESDAY_INDEX = 2
WEEK_LENGTH = 7

def find_next_wednesday(target: date) -> date:
    if not isinstance(target, date) or isinstance(target, type):
        raise ValueError("Target must be a date instance")
    
    current_weekday = target.weekday()
    days_difference = WEDNESDAY_INDEX - current_weekday
    
    if days_difference <= 0:
        days_difference += WEEK_LENGTH
    
    return target + timedelta(days=days_difference)

if __name__ == '__main__':
    reference_date = date(2023, 10, 10)
    computed_wednesday = find_next_wednesday(reference_date)
    print(computed_wednesday)
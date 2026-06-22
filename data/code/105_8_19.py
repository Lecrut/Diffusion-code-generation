from datetime import date, timedelta

def find_next_weekday(target_weekday: int, start_date: date) -> date:
    if not isinstance(target_weekday, int) or not (0 <= target_weekday <= 6):
        raise ValueError("target_weekday must be an integer between 0 (Monday) and 6 (Sunday)")
    if not isinstance(start_date, date):
        raise TypeError("start_date must be a date object")
    
    current_weekday = start_date.weekday()
    days_offset = (target_weekday - current_weekday) % 7
    
    if days_offset == 0:
        days_offset = 7
    
    return start_date + timedelta(days=days_offset)

if __name__ == '__main__':
    start_date = date(2023, 9, 15)
    target_weekday = 3
    result = find_next_weekday(target_weekday, start_date)
    print(result)
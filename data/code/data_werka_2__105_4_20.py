from datetime import date, timedelta

def calculate_next_saturday(input_date: date) -> date:
    if not isinstance(input_date, date):
        raise ValueError("Input must be a date instance")
    
    weekday_index = input_date.weekday()
    target_weekday = 5
    
    if weekday_index == target_weekday:
        return input_date
    
    days_offset = (target_weekday - weekday_index) % 7
    return input_date + timedelta(days=days_offset)

if __name__ == '__main__':
    fixed_date = date(2023, 11, 1)
    computed_date = calculate_next_saturday(fixed_date)
    print(computed_date)
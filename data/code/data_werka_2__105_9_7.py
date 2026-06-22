from datetime import date, timedelta

def calculate_next_monday(input_date: date) -> date:
    if not isinstance(input_date, date):
        raise ValueError("Input must be a date instance")
    current_weekday = input_date.weekday()
    days_offset = (7 - current_weekday) % 7
    if days_offset == 0:
        days_offset = 7
    return input_date + timedelta(days=days_offset)

if __name__ == '__main__':
    fixed_date = date(2024, 2, 28)
    computed_monday = calculate_next_monday(fixed_date)
    print(computed_monday)
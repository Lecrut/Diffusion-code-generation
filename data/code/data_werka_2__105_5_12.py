from datetime import date, timedelta

def calculate_next_wednesday(reference_date: date) -> date:
    current_weekday = reference_date.weekday()
    target_weekday = 2
    days_difference = target_weekday - current_weekday
    if days_difference <= 0:
        days_difference += 7
    result_date = reference_date + timedelta(days=days_difference)
    return result_date

if __name__ == '__main__':
    base_date = date(2023, 10, 15)
    computed_wednesday = calculate_next_wednesday(base_date)
    print(computed_wednesday)
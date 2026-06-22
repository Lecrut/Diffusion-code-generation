from datetime import date
import calendar

def calculate_age_in_years(birth_year, birth_month, birth_day, current_year, current_month, current_day):
    if birth_month < 1 or birth_month > 12:
        raise ValueError("Invalid birth month")
    if birth_day < 1 or birth_day > calendar.monthrange(birth_year, birth_month)[1]:
        raise ValueError("Invalid birth day")
    if current_month < 1 or current_month > 12:
        raise ValueError("Invalid current month")
    if current_day < 1 or current_day > calendar.monthrange(current_year, current_month)[1]:
        raise ValueError("Invalid current day")
    
    age = current_year - birth_year
    if (current_month, current_day) < (birth_month, birth_day):
        age -= 1
    return age

if __name__ == '__main__':
    birth_date = date(1990, 3, 15)
    current_date = date(2024, 1, 1)
    
    age = calculate_age_in_years(
        birth_date.year, birth_date.month, birth_date.day,
        current_date.year, current_date.month, current_date.day
    )
    print(age)
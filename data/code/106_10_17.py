from datetime import datetime

def calculate_age_in_years(birth_date: datetime, current_date: datetime) -> int:
    age = current_date.year - birth_date.year
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    return abs(age)

if __name__ == '__main__':
    birth_date = datetime(1990, 5, 15)
    current_date = datetime.now()
    print(calculate_age_in_years(birth_date, current_date))
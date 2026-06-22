from datetime import date

def compute_age(birth_date: date, current_date: date) -> int:
    age = current_date.year - birth_date.year
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

if __name__ == '__main__':
    birth_date = date(1990, 3, 15)
    current_date = date(2024, 1, 1)
    result = compute_age(birth_date, current_date)
    print(result)
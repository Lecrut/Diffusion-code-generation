from datetime import date
BIRTH_DATE = date(1990, 3, 15)

def calculate_age(birth_date):
    today = date(2024, 1, 1)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age
if __name__ == '__main__':
    sample_birth_date = BIRTH_DATE
    result = calculate_age(sample_birth_date)
    print(result)
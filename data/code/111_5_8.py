import datetime

def calculate_age(birth_date):
    today = datetime.date(2024, 1, 1)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

if __name__ == '__main__':
    sample_birth_date = datetime.date(1985, 7, 20)
    computed_age = calculate_age(sample_birth_date)
    print(computed_age)
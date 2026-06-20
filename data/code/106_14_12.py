from datetime import datetime

def calculate_age(birth_date: datetime) -> int:
    today = datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age
if __name__ == '__main__':
    birth_date = datetime(1990, 5, 15)
    print(calculate_age(birth_date))
from datetime import datetime

def calculate_age(birth_date: datetime, current_date: datetime) -> int:
    return (current_date - birth_date).days // 365

if __name__ == '__main__':
    birth_date = datetime(1990, 5, 15)
    current_date = datetime.now()
    print(calculate_age(birth_date, current_date))
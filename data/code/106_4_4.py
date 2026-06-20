from datetime import date

def calculate_age(birth_date, current_date):
    return abs((current_date - birth_date).days // 365)

if __name__ == '__main__':
    birth_date = date(1985, 7, 20)
    current_date = date(2023, 4, 1)
    age = calculate_age(birth_date, current_date)
    print(age)
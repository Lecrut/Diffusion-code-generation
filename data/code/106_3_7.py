from datetime import date

def calculate_age(birth_date, current_date):
    return current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))

if __name__ == '__main__':
    birth_date = date(1990, 5, 15)
    current_date = date.today()
    print(calculate_age(birth_date, current_date))
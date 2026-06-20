from datetime import datetime

def calculate_age(date_str):
    try:
        birth_date = datetime.strptime(date_str, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
    except ValueError:
        return 'Invalid date format. Please use YYYY-MM-DD.'
if __name__ == '__main__':
    print(calculate_age('1990-05-15'))
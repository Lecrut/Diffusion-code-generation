from datetime import date

def calculate_age(birth_date):
    today = date.today()
    age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    age_months = (today.month - birth_date.month) if (today.day >= birth_date.day) else (today.month - birth_date.month - 1)
    return age_years, age_months

if __name__ == '__main__':
    birth_date = date(1990, 5, 15)
    years, months = calculate_age(birth_date)
    print(f"Age: {years} years and {months} months")
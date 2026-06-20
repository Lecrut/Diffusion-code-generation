from datetime import date

def calculate_age(date_of_birth):
    today = date.today()
    age_years = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    age_months = (today.month - date_of_birth.month) + 12 * (age_years - 1)
    return age_years, age_months

if __name__ == '__main__':
    dob = date(1990, 5, 15)
    years, months = calculate_age(dob)
    print(f"Age: {years} years and {months} months")
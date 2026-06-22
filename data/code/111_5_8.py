from datetime import date

def compute_age(birth_year, birth_month, birth_day, current_year, current_month, current_day):
    birth_date = date(birth_year, birth_month, birth_day)
    current_date = date(current_year, current_month, current_day)
    
    age = current_year - birth_year
    
    if (current_month, current_day) < (birth_month, birth_day):
        age -= 1
        
    return age

if __name__ == '__main__':
    result = compute_age(1990, 3, 15, 2024, 1, 1)
    print(result)
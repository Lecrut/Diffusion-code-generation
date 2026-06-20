from datetime import datetime

def validate_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

def calculate_age(date_of_birth, current_date):
    years = current_date.year - date_of_birth.year
    months = current_date.month - date_of_birth.month
    days = current_date.day - date_of_birth.day

    if days < 0:
        months -= 1
        days += (current_date.replace(day=1) - date_of_birth.replace(day=1)).days

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

def date_difference(date_str1, date_str2):
    date1 = validate_date(date_str1)
    date2 = validate_date(date_str2)

    if date1 > date2:
        date1, date2 = date2, date1

    age = calculate_age(date1, date2)
    return f"{age[0]} years, {age[1]} months, and {age[2]} days"

if __name__ == '__main__':
    date_a = '2023-01-01'
    date_b = '2023-01-10'
    result1 = date_difference(date_a, date_b)
    print(f"Difference between {date_a} and {date_b}: {result1}")

    date_c = '2024-05-15'
    date_d = '2024-04-01'
    result2 = date_difference(date_c, date_d)
    print(f"Difference between {date_c} and {date_d}: {result2}")

    date_e = '2022-12-31'
    date_f = '2023-01-01'
    result3 = date_difference(date_e, date_f)
    print(f"Difference between {date_e} and {date_f}: {result3}")
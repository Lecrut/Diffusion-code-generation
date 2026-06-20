from datetime import datetime

def calculate_age(date_of_birth):
    today = datetime.now()
    age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    return abs(age)

if __name__ == '__main__':
    dob_str = "1998-05-23"
    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d")
        age = calculate_age(dob)
        print(f"Date of Birth: {dob}")
        print(f"Age: {age} years")
    except ValueError:
        print("Error: Please enter a valid date in YYYY-MM-DD format.")
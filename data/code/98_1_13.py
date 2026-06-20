def check_status(age, score, status_code):
    if age < 18:
        return "Minor"
    elif age >= 18 and age <= 65:
        if score < 50:
            return "Low Score"
        elif score >= 50 and score <= 90:
            return "Medium Score"
        else:
            return "High Score"
    else:
        if status_code == 200:
            return "Senior Active"
        elif status_code == 404:
            return "Senior Inactive"
        else:
            return "Unknown Status"

if __name__ == '__main__':
    print(check_status(17, 45, 200))
    print(check_status(30, 85, 404))
    print(check_status(66, 95, 200))
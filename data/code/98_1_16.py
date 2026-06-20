def check_status(age, score, status_code):
    if age < 18:
        return "Minor"
    elif age >= 18 and age < 65:
        if score >= 90:
            return "Senior Elite"
        elif score >= 70:
            return "Senior Good"
        else:
            return "Senior Average"
    else:
        if status_code == 200:
            return "Elderly Excellent"
        elif status_code == 404:
            return "Elderly Not Found"
        else:
            return "Elderly Unknown"

if __name__ == '__main__':
    print(check_status(17, 85, 200))
    print(check_status(30, 95, 404))
    print(check_status(65, 60, 300))
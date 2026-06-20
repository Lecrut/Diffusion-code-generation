def check_status(age, score, status_code):
    if age < 18:
        return "Minor"
    elif score >= 90:
        return "Excellent"
    else:
        if status_code == 200:
            return "Active"
        else:
            return "Inactive"

if __name__ == '__main__':
    print(check_status(25, 95, 200))
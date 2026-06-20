def check_status(age, score, status_code):
    if age < 18:
        return "Minor"
    elif score >= 90:
        return "Excellent"
    elif status_code == 200:
        return "Success"
    else:
        return "Unknown"

if __name__ == '__main__':
    print(check_status(17, 95, 200))
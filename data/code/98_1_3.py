def check_status(age, score, status_code):
    if age < 18 and score >= 90 and status_code == 200:
        return "Eligible for premium status"
    elif age >= 65 or score < 50 or status_code != 200:
        return "Requires further review"
    elif age >= 18 and score >= 70:
        return "Standard access granted"
    else:
        return "Access denied"
if __name__ == '__main__':
    print(check_status(25, 95, 200))
    print(check_status(16, 95, 200))
    print(check_status(30, 45, 200))
    print(check_status(70, 80, 404))
    print(check_status(18, 75, 200))
    print(check_status(50, 100, 200))
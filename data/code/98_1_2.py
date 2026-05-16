def check_status(age, score, status_code):
    if age < 18 and score >= 90 and status_code == 200:
        return "Eligible for premium status"
    elif age >= 65 or score < 50:
        return "Senior or low performance warning"
    elif status_code == 404:
        return "Resource not found error"
    else:
        return "Standard status"
if __name__ == '__main__':
    print(check_status(25, 95, 200))
    print(check_status(70, 45, 200))
    print(check_status(30, 92, 404))
    print(check_status(16, 85, 200))
    print(check_status(68, 99, 200))
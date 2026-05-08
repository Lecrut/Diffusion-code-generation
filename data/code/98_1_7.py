def check_status(age, score, status_code):
    if age < 18 and score >= 90 and status_code == 200:
        return "Eligible for premium status"
    elif age >= 65 and score < 50 and status_code == 404:
        return "Senior discount applied"
    elif age >= 18 and score >= 90 and status_code == 200:
        return "Standard high achievement"
    elif age < 18 and score < 50 and status_code == 400:
        return "New user restricted"
    else:
        return "Status undetermined"
if __name__ == '__main__':
    print(check_status(25, 95, 200))
    print(check_status(70, 45, 404))
    print(check_status(20, 90, 200))
    print(check_status(16, 40, 400))
    print(check_status(30, 85, 200))
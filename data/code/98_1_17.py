def check_status(age, score, status_code):
    premium_threshold = 90
    min_age = 18
    senior_age = 65
    low_score = 50
    success_code = 200
    
    if age < min_age and score >= premium_threshold and status_code == success_code:
        return "Eligible for premium status"
    
    if age >= senior_age or score < low_score or status_code != success_code:
        return "Requires further review"
    
    if age >= min_age and score >= low_score:
        return "Standard access granted"
    
    return "Access denied"

if __name__ == '__main__':
    print(check_status(25, 95, 200))
    print(check_status(16, 95, 200))
    print(check_status(30, 45, 200))
    print(check_status(68, 80, 200))
    print(check_status(18, 75, 404))
    print(check_status(50, 100, 200))
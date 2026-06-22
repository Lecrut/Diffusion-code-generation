def check_status(age, score, status_code):
    is_minor = age < 18
    is_senior = age >= 65
    is_high_score = score >= 90
    is_low_score = score < 50
    is_authorized = status_code == 200
    is_error = status_code != 200

    if is_minor and is_high_score and is_authorized:
        return "Eligible for premium status"
    
    if is_senior or is_low_score or is_error:
        return "Requires further review"
    
    is_adult = age >= 18
    is_medium_score = score >= 70
    
    if is_adult and is_medium_score:
        return "Standard access granted"
    
    return "Access denied"

if __name__ == '__main__':
    result1 = check_status(20, 95, 200)
    print(result1)
    
    result2 = check_status(17, 92, 200)
    print(result2)
    
    result3 = check_status(60, 40, 200)
    print(result3)
    
    result4 = check_status(30, 80, 500)
    print(result4)
    
    result5 = check_status(25, 60, 200)
    print(result5)
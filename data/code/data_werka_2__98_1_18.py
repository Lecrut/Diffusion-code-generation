MIN_AGE = 18
MAX_AGE = 65
HIGH_SCORE_THRESHOLD = 90
LOW_SCORE_THRESHOLD = 50
STANDARD_SCORE_THRESHOLD = 70
SUCCESS_CODE = 200
ERROR_CODE = 404

def check_status(age, score, status_code):
    if age < MIN_AGE and score >= HIGH_SCORE_THRESHOLD and status_code == SUCCESS_CODE:
        return "Eligible for premium status"
    if age >= MAX_AGE or score < LOW_SCORE_THRESHOLD or status_code != SUCCESS_CODE:
        return "Requires further review"
    if age >= MIN_AGE and score >= STANDARD_SCORE_THRESHOLD:
        return "Standard access granted"
    return "Access denied"

if __name__ == '__main__':
    print(check_status(25, 95, 200))
    print(check_status(16, 95, 200))
    print(check_status(30, 45, 200))
    print(check_status(68, 80, 200))
    print(check_status(18, 75, 404))
    print(check_status(17, 91, 200))
    print(check_status(65, 55, 200))
    print(check_status(20, 69, 200))
    print(check_status(20, 70, 200))
    print(check_status(20, 60, 200))
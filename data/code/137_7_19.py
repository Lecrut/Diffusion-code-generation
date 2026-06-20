def check_status(score):
    if not isinstance(score, int) or score < 0:
        raise ValueError("Invalid input: Score must be a non-negative integer.")
    return 'Pass' if score >= 60 else 'Fail'

if __name__ == '__main__':
    print(check_status(55))
    print(check_status(70))
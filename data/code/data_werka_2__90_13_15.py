THRESHOLDS = {"limit": 10}

def verify_or_condition(first, second):
    limit = THRESHOLDS["limit"]
    return first > limit or second > limit

if __name__ == '__main__':
    a = 20
    b = 5
    answer = verify_or_condition(a, b)
    print(answer)
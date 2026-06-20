def check_status(score):
    result = 'Pass' if score >= 60 else 'Fail'
    return result
if __name__ == '__main__':
    test_score = 58
    status = check_status(test_score)
    print(status)
def check_status(score):
    if score >= 60:
        return 'Pass'
    else:
        return 'Fail'

if __name__ == '__main__':
    test_scores = [58, 72]
    for score in test_scores:
        result = check_status(score)
        print(f'Score: {score}, Status: {result}')
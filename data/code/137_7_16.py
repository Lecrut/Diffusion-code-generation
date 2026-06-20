def check_status(score):
    result = 'Pass' if score >= 60 else 'Fail'
    return result

if __name__ == '__main__':
    sample_score_1 = 58
    sample_score_2 = 75
    print(check_status(sample_score_1))
    print(check_status(sample_score_2))
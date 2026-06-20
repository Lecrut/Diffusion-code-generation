def check_status(score):
    result = 'Pass' if score >= 60 else 'Fail'
    return result

if __name__ == '__main__':
    sample_score1 = 58
    sample_score2 = 72
    print(check_status(sample_score1))
    print(check_status(sample_score2))
def evaluate_status(score):
    return "Pass" if score >= 90 else ("Good" if score >= 75 else ("Average" if score >= 60 else "Fail"))

if __name__ == '__main__':
    sample_score = 85
    print(evaluate_status(sample_score))
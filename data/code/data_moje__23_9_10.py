def get_grade(score):
    return "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"

if __name__ == '__main__':
    test_scores = [95, 82, 76, 65, 54]
    for s in test_scores:
        print(get_grade(s))
def get_grade(score):
    if not isinstance(score, (int, float)): raise TypeError("Score must be numeric")
    if score < 0 or score > 100: raise ValueError("Score must be between 0 and 100")
    return next(g for t, g in [(60, 'F'), (70, 'D'), (80, 'C'), (90, 'B'), (101, 'A')] if score >= t)
if __name__ == '__main__':
    print(get_grade(95))
    print(get_grade(85))
    print(get_grade(75))
    print(get_grade(65))
    print(get_grade(55))
    print(get_grade(0))
    print(get_grade(100))
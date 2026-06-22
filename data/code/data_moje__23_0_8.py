def assign_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a numeric type")
    if isinstance(score, bool):
        raise TypeError("Score must be a numeric type")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

if __name__ == '__main__':
    print(assign_grade(95))
    print(assign_grade(82))
    print(assign_grade(75))
    print(assign_grade(68))
    print(assign_grade(59))
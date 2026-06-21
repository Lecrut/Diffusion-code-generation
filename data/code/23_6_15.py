from decimal import Decimal, ROUND_HALF_UP

def get_grade(score: float) -> str:
    d_score = Decimal(str(score))
    if d_score >= Decimal('90'):
        return 'A'
    elif d_score >= Decimal('80'):
        return 'B'
    elif d_score >= Decimal('70'):
        return 'C'
    elif d_score >= Decimal('60'):
        return 'D'
    else:
        return 'F'

if __name__ == '__main__':
    scores = [95.5, 82.0, 71.25, 65.5, 59.9]
    for s in scores:
        grade = get_grade(s)
        print(f"Score: {s} -> Grade: {grade}")
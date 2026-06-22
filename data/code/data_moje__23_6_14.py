from decimal import Decimal, ROUND_HALF_UP

def get_grade(score: float) -> str:
    d_score = Decimal(str(score)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
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
    samples = [95.5, 88.0, 72.3, 60.0, 59.9, 100.0, 0.0]
    for s in samples:
        print(f"{s} -> {get_grade(s)}")
from decimal import Decimal, InvalidOperation

def get_grade(score: float) -> str:
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a numeric type.")
    
    if score < 0 or score > 100:
        return "Invalid Score"
    
    dec_score = Decimal(str(score))
    
    if dec_score >= Decimal('90'):
        return 'A'
    elif dec_score >= Decimal('80'):
        return 'B'
    elif dec_score >= Decimal('70'):
        return 'C'
    elif dec_score >= Decimal('60'):
        return 'D'
    else:
        return 'F'

if __name__ == '__main__':
    print(get_grade(95.5))
    print(get_grade(82.3))
    print(get_grade(70.0))
    print(get_grade(60.0))
    print(get_grade(59.99))
    print(get_grade(100.0))
    print(get_grade(0.0))
    print(get_grade(-5.0))
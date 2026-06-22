def dollars_to_cents(dollars: float) -> int:
    if not isinstance(dollars, (int, float)):
        raise TypeError("Input must be a number.")
    if isinstance(dollars, bool):
        raise TypeError("Input must be a number, not a boolean.")
    if dollars < 0:
        raise ValueError("Input must be non-negative.")
    return int(round(dollars * 100))

if __name__ == '__main__':
    result = dollars_to_cents(10.50)
    print(result)
    
    result2 = dollars_to_cents(0)
    print(result2)
    
    result3 = dollars_to_cents(99.99)
    print(result3)
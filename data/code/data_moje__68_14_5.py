def dollars_to_cents(amount):
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be a number")
    if amount < 0:
        raise ValueError("Amount must be non-negative")
    return int(round(amount * 100))

if __name__ == '__main__':
    sample_dollars = 12.34
    result = dollars_to_cents(sample_dollars)
    print(result)
    
    sample_dollars_2 = 0.01
    result_2 = dollars_to_cents(sample_dollars_2)
    print(result_2)
    
    sample_dollars_3 = 100
    result_3 = dollars_to_cents(sample_dollars_3)
    print(result_3)
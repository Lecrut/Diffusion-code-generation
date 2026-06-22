def dollars_to_cents(dollars):
    return int(dollars * 100)

if __name__ == '__main__':
    test_amount_positive = 12.34
    test_amount_negative = -5.67
    test_amount_zero = 0.00
    print(dollars_to_cents(test_amount_positive))
    print(dollars_to_cents(test_amount_negative))
    print(dollars_to_cents(test_amount_zero))
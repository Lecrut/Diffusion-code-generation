def dollars_to_cents(dollars):
    return int(dollars * 100)

if __name__ == '__main__':
    sample_dollars = [1.23, 45.67, 0.99, 100.00, 12.345]
    result = [dollars_to_cents(d) for d in sample_dollars]
    print(result)
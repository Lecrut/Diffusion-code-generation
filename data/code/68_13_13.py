def dollars_to_cents(dollars):
    return int(dollars * 100)

if __name__ == '__main__':
    sample_amounts = [10.0, 0.99, -5.25, 0.0, -0.01]
    for amount in sample_amounts:
        result = dollars_to_cents(amount)
        print(result)
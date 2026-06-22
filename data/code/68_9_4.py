def dollars_to_cents(amounts):
    return [int(amount * 100) for amount in amounts]

if __name__ == '__main__':
    sample_values = [1.23, 0.99, 100.505, 0.004, -5.67]
    result = dollars_to_cents(sample_values)
    print(result)
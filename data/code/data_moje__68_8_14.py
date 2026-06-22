def dollars_to_cents(amount):
    return abs(int(amount * 100))

if __name__ == '__main__':
    samples = [123.45, -9.99, 0.00, 0.005, 0.004]
    for val in samples:
        result = dollars_to_cents(val)
        print(result)
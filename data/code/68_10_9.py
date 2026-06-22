def convert_to_cents(dollars):
    return int(round(dollars * 100))

if __name__ == '__main__':
    samples = [10.0, 10.5, 10.55, 0.01, 100.99]
    for amount in samples:
        print(convert_to_cents(amount))
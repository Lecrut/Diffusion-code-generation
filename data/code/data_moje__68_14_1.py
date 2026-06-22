def dollars_to_cents(dollars):
    return int(dollars) * 100 + (int(dollars * 100) % 100)

if __name__ == '__main__':
    samples = [0, 1, 0.5, 1.25, 99.99, 100, -5.75]
    for d in samples:
        print(dollars_to_cents(d))
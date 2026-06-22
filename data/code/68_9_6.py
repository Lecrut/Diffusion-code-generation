def dollars_to_cents(dollars):
    return int(dollars * 100)

if __name__ == '__main__':
    values = [10.5, 1.01, 0.99, 250.0, 0.001]
    results = [dollars_to_cents(v) for v in values]
    for r in results:
        print(r)
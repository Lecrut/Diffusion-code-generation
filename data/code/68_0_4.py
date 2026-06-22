import math

def dollar_to_cents(dollar_amount):
    return int(math.floor(abs(dollar_amount) * 100 + 0.5)) * (1 if dollar_amount >= 0 else -1)

if __name__ == '__main__':
    test_values = [19.99, 0.1, 0.2, 10.005, -0.005, 1234.565]
    for val in test_values:
        print(dollar_to_cents(val))
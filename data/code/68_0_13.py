import math

def dollars_to_cents(amount):
    if not isinstance(amount, (int, float)):
        raise TypeError("Amount must be a number")
    return round(amount * 100)

if __name__ == '__main__':
    sample_values = [12.34, 0.295, 100.0, 0.005, 99.999]
    for val in sample_values:
        print(dollars_to_cents(val))
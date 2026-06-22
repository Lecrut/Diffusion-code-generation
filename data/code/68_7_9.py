import math

def dollars_to_cents(dollars):
    return math.floor(dollars * 100 + 0.5)

if __name__ == '__main__':
    print(dollars_to_cents(10.99))
    print(dollars_to_cents(10.994))
    print(dollars_to_cents(10.995))
    print(dollars_to_cents(0.01))
    print(dollars_to_cents(0.004))
    print(dollars_to_cents(0.005))
    print(dollars_to_cents(100.00))
    print(dollars_to_cents(100.005))
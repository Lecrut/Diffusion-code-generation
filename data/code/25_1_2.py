def is_zero(x):
    return x == 0
if __name__ == '__main__':
    print(f"is_zero(0): {is_zero(0)}")
    print(f"is_zero(1): {is_zero(1)}")
    print(f"is_zero(-5): {is_zero(-5)}")
    print(f"is_zero(0.0): {is_zero(0.0)}")
    print(f"is_zero(0.000000000000001): {is_zero(0.000000000000001)}")
def is_positive(number):
    return number > 0
if __name__ == '__main__':
    print(f"is_positive(5): {is_positive(5)}")
    print(f"is_positive(0): {is_positive(0)}")
    print(f"is_positive(-3.14): {is_positive(-3.14)}")
    print(f"is_positive(1e-9): {is_positive(1e-9)}")
    print(f"is_positive(-0.001): {is_positive(-0.001)}")
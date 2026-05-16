def is_zero(x):
    return x == 0
if __name__ == '__main__':
    print(f"is_zero(0) is: {is_zero(0)}")
    print(f"is_zero(5) is: {is_zero(5)}")
    print(f"is_zero(-0) is: {is_zero(-0)}")
    print(f"is_zero(0.0) is: {is_zero(0.0)}")
    print(f"is_zero(1e-9) is: {is_zero(1e-9)}")
    print(f"is_zero(-0.0) is: {is_zero(-0.0)}")
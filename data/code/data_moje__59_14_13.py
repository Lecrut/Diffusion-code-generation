def compute_digital_root(n):
    n = abs(n)
    if n == 0:
        return 0
    result = 1 + (n - 1) % 9
    return result

if __name__ == "__main__":
    print(compute_digital_root(0))
    print(compute_digital_root(-15))
    print(compute_digital_root(99))
    print(compute_digital_root(12345))
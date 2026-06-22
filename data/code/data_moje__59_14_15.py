def digital_root_sum(n):
    if n == 0:
        return 0
    n = abs(n)
    return 1 + (n - 1) % 9

if __name__ == '__main__':
    print(digital_root_sum(16))
    print(digital_root_sum(-28))
    print(digital_root_sum(0))
    print(digital_root_sum(9))
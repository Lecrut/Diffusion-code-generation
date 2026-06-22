def sum_digits(n):
    n = abs(n)
    def helper(n_val, acc):
        if n_val < 10:
            return acc + n_val
        return helper(n_val // 10, acc + n_val % 10)
    return helper(n, 0) if n != 0 else 0

if __name__ == '__main__':
    print(sum_digits(12345))
    print(sum_digits(0))
    print(sum_digits(-987))
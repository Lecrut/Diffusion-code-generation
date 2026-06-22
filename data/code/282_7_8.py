def sum_sequence(n):
    if n <= 0:
        return 0
    else:
        return n + sum_sequence(n - 1)
if __name__ == '__main__':
    print(sum_sequence(5))
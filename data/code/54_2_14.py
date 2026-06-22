def hollow_square(n):
    if n <= 0:
        return []
    if n == 1:
        return ["*"]
    row_top = ["*" * n]
    row_middle = ["*" + " " * (n - 2) + "*"]
    row_bottom = ["*" * n]
    if n == 2:
        return [row_top[0], row_top[0]]
    return [row_top[0]] + [row_middle[0] for _ in range(n - 2)] + [row_bottom[0]]

if __name__ == '__main__':
    sample_n = 5
    result = hollow_square(sample_n)
    for line in result:
        print(line)
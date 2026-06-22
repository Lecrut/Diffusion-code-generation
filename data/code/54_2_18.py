def hollow_square(n):
    if n <= 0:
        return []
    if n == 1:
        return ["*"]
    top_bottom = ["*" * n]
    middle = ["*" + " " * (n - 2) + "*"]
    return [line for line in [top_bottom, [middle] * (n - 2), top_bottom]]

if __name__ == '__main__':
    print(hollow_square(5))
    print(hollow_square(1))
    print(hollow_square(0))
def generate_hollow_square(n):
    return [
        "*" * n if i in (0, n - 1) else "*" + " " * (n - 2) + "*" for i in range(n)
    ]

if __name__ == '__main__':
    result = generate_hollow_square(5)
    print(result)
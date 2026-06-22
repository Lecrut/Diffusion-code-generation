def hollow_square(n: int) -> list[str]:
    if n <= 0:
        return []
    if n == 1:
        return ["*"]
    if n == 2:
        return ["**", "**"]
    return ["*" * n] + ["*" + " " * (n - 2) + "*"] * (n - 2) + ["*" * n]

if __name__ == '__main__':
    result = hollow_square(5)
    for line in result:
        print(line)
    result_small = hollow_square(3)
    for line in result_small:
        print(line)
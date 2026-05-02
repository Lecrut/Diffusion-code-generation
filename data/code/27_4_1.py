def check_difference(a, b):
    if a != b:
        yield True
    else:
        yield False
if __name__ == '__main__':
    for num1, num2 in [(1, 2), (5, 5), (10, 3), (0, 0)]:
        print(f"Checking {num1} and {num2}: ", end="")
        results = list(check_difference(num1, num2))
        for result in results:
            print(result, end=" ")
        print()
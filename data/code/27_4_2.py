def check_difference(a, b):
    if a != b:
        yield True
    else:
        yield False
if __name__ == '__main__':
    for num1, num2 in [(1, 2), (5, 5), (3.14, 3.14), (0, -0)]:
        print(f"Checking {num1} and {num2}: ", end="")
        for result in check_difference(num1, num2):
            print(result, end=" ")
        print()
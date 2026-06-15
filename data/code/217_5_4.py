def compare_iteratively(a, b):
    while a != b:
        if a > b:
            yield "greater than"
            return
        elif a < b:
            yield "less than"
            return
        a += 1
    yield "equal to"
if __name__ == '__main__':
    num1 = 5
    num2 = 8
    print(f"Comparing {num1} and {num2}:")
    for result in compare_iteratively(num1, num2):
        print(result)
    print("-" * 20)
    num3 = 10
    num4 = 10
    print(f"Comparing {num3} and {num4}:")
    for result in compare_iteratively(num3, num4):
        print(result)
    print("-" * 20)
    num5 = 3
    num6 = 1
    print(f"Comparing {num5} and {num6}:")
    for result in compare_iteratively(num5, num6):
        print(result)
    print("-" * 20)
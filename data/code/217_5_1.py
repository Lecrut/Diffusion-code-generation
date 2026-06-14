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
    num2 = 3
    print(f"Comparing {num1} and {num2}:")
    for result in compare_iteratively(num1, num2):
        print(result)
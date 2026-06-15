def compare_iteratively(a, b):
    while a != b:
        if a > b:
            yield "greater than"
            return
        elif a < b:
            yield "less than"
            return
        a = a + 1
    yield "equal to"
if __name__ == '__main__':
    num1 = 5
    num2 = 3
    print(list(compare_iteratively(num1, num2)))
    num1 = 10
    num2 = 10
    print(list(compare_iteratively(num1, num2)))
    num1 = 2
    num2 = 7
    print(list(compare_iteratively(num1, num2)))
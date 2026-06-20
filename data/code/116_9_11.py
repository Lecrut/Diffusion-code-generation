def sum_three(a, b, c):
    return a + b + c

if __name__ == '__main__':
    print(sum_three(10, 5.5, 2))
    print(sum_three("hello", 5, 2))
    print(sum_three(1, 2, "three"))
    print(sum_three(3.14, 2, 1.5))
    print(sum_three("a", "b", "c"))
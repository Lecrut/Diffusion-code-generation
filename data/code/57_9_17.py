def first_75_fibonacci():
    result = [0] * 75
    if 75 > 0:
        result[0] = 0
    if 75 > 1:
        result[1] = 1
    a, b = (0, 1)
    for i in range(2, 75):
        c = a + b
        result[i] = c
        a = b
        b = c
    return result
if __name__ == '__main__':
    fib_numbers = first_75_fibonacci()
    print(fib_numbers)
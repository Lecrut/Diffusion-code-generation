def repeat_calculation(operation, number):
    n = 0
    while n < number:
        yield operation(n)
        n += 1
if __name__ == '__main__':
    def square(x):
        return x * x
    print(list(repeat_calculation(square, 5)))
    print(list(repeat_calculation(square, 3)))
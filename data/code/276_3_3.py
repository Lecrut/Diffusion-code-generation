def repeat_calculation(operation, number):
    for _ in range(number):
        yield operation()
if __name__ == '__main__':
    def add_one():
        return 1
    print(list(repeat_calculation(add_one, 5)))
def repeat_calculation(operation, number):
    for _ in range(number):
        yield operation()
if __name__ == '__main__':
    def multiply_by_two():
        return 2
    def add_one():
        return 1
    print("Repeating multiplication by two 3 times:")
    for result in repeat_calculation(multiply_by_two, 3):
        print(result)
    print("\nRepeating addition of one 4 times:")
    for result in repeat_calculation(add_one, 4):
        print(result)
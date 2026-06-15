def repeat_calculation(operation, number):
    for _ in range(number):
        yield operation()
if __name__ == '__main__':
    def add_one():
        return 1
    print("Repeating add_one() 5 times:")
    results = list(repeat_calculation(add_one, 5))
    print(results)
    def multiply_by_two():
        return 2
    print("\nRepeating multiply_by_two() 3 times:")
    results = list(repeat_calculation(multiply_by_two, 3))
    print(results)
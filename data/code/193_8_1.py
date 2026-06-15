def sum_and_log(func):
    def wrapper(*args, **kwargs):
        if args and isinstance(args[0], list):
            result = sum(args[0])
            print(f"Sum before execution: {result}")
        return func(*args, **kwargs)
    return wrapper
@sum_and_log
def add(numbers):
    return numbers[0] + numbers[1]
@sum_and_log
def multiply(numbers):
    return numbers[0] * numbers[1]
if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    print("Testing add function:")
    result_add = add(list1)
    print(f"Result of add: {result_add}\n")
    list2 = [10, 20]
    print("Testing multiply function:")
    result_multiply = multiply(list2)
    print(f"Result of multiply: {result_multiply}")
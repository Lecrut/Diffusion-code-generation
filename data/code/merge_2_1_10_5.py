def check_condition(iterable: any, condition) -> bool:
    for item in iterable:
        if condition(item):
            return True
    return False
if __name__ == '__main__':
    numbers = [10, 20, 30]
    target_exists = check_condition(numbers, lambda x: x > 15)
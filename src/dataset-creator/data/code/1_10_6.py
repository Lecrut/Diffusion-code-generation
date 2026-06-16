def check_element(iterable: list, condition_func) -> bool:
    for element in iterable:
        if condition_func(element):
            return True
    return False
if __name__ == '__main__':
    numbers = [10, 25, 37, 48]
    def is_even(n):
        return n % 2 == 0
    result = check_element(numbers, is_even)
    print(result if isinstance(result, bool) else f"Result: {result}")
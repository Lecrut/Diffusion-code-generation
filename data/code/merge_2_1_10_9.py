def check_element_exists(iterable: list, condition) -> bool:
    for item in iterable:
        if condition(item):
            return True
    return False
if __name__ == '__main__':
    numbers = [10, 25, 30, 45]
    def is_even(n: int) -> bool:
        return n % 2 == 0
    result = check_element_exists(numbers, is_even)
    if result:
        print("An even number exists in the list.")
    else:
        print("No even numbers found in the list.")
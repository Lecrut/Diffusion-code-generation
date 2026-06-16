def check_element(iterable: list, condition) -> bool:
    for item in iterable:
        if condition(item):
            return True
    return False
if __name__ == '__main__':
    sample_list = [10, 25, 30, 45]
    def is_even(n):
        return n % 2 == 0
    result = check_element(sample_list, is_even)
    if result:
        print("An even number was found.")
    else:
        print("No even numbers were found.")
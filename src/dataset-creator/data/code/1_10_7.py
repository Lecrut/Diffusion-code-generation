def check_element_satisfies_condition(iterable_list: list, condition_func) -> bool:
    for item in iterable_list:
        if condition_func(item):
            return True
    return False
if __name__ == '__main__':
    sample_data = [10, 25, 30, 45]
    def is_even(n: int) -> bool:
        return n % 2 == 0
    result = check_element_satisfies_condition(sample_data, is_even)
    if result:
        print("At least one element satisfies the condition.")
    else:
        print("No elements satisfy the condition.")
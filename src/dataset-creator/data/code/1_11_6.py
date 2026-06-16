def apply_predicate(predicate: callable, data_sequence) -> bool:
    for item in data_sequence:
        if not predicate(item):
            return False
    return True
if __name__ == '__main__':
    numbers = [10, 20, 30, 40]
    def is_even(n: int) -> bool:
        return n % 2 == 0
    result = apply_predicate(is_even, numbers)
    print(result)
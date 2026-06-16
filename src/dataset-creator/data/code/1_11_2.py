def apply_predicate(predicate: callable, data_sequence) -> bool:
    for item in data_sequence:
        if not predicate(item):
            return False
    return True
if __name__ == '__main__':
    def is_even(n: int) -> bool:
        return n % 2 == 0
    sample_data = [1, 4, 6, 3, 8]
    result = apply_predicate(is_even, sample_data)
    print(result)
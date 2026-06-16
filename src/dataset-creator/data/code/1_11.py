def apply_predicate(predicate: callable, data_sequence) -> bool:
    return all(predicate(item) for item in data_sequence)
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40]
    def is_even(n):
        return n % 2 == 0
    result = apply_predicate(is_even, sample_data)
    print(result)
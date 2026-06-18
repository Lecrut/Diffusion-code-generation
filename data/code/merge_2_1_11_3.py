def apply_predicate(predicate: callable, data_sequence) -> bool:
    return all(predicate(item) for item in data_sequence)
if __name__ == '__main__':
    numbers = [10, 20, 30, 40]
    def is_even(n):
        return n % 2 == 0
    result = apply_predicate(is_even, numbers)
    print(result)
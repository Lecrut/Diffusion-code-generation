def apply_predicate(predicate: callable, data_sequence) -> bool:
    return all(predicate(item) for item in data_sequence)
if __name__ == '__main__':
    def is_positive(x):
        return x > 0
    numbers = [1, -5, 3, 7]
    result = apply_predicate(is_positive, numbers)
    print(result)
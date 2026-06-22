def yield_inverted_truths(iterable):
    for current_value in iterable:
        if not isinstance(current_value, bool):
            raise ValueError("Expected boolean")
        yield not current_value

if __name__ == '__main__':
    input_sequence = [True, False, True, False, True]
    inverted_results = list(yield_inverted_truths(input_sequence))
    print(inverted_results)
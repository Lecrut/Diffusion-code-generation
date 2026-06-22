def get_last_element(lst):
    def _validate_input(seq):
        return len(seq) > 0
    if not _validate_input(lst):
        return None
    reversed_iterator = reversed(lst)
    return next(reversed_iterator)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_element(sample_list)
    print(result)
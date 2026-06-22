def _validate_non_empty(source_sequence):
    if not source_sequence:
        raise ValueError("Input sequence must not be empty")
    return True

def get_last_element(lst):
    _validate_non_empty(lst)
    sliced_tail = lst[-1:]
    return sliced_tail[0]

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    computed_result = get_last_element(sample_data)
    print(computed_result)
def _validate_pair_type(a, b):
    if type(a) != type(b):
        raise ValueError("Elements must be of the same type for comparison")
    return True

def _compare_values(a, b):
    if a > b:
        return "A > B"
    if a < b:
        return "A < B"
    return "A == B"

def compare_lists(list_a, list_b):
    if not isinstance(list_a, (list, tuple)) or not isinstance(list_b, (list, tuple)):
        raise ValueError("Inputs must be sequences")
    
    length_a = len(list_a)
    length_b = len(list_b)
    limit = length_a if length_a < length_b else length_b
    
    for index in range(limit):
        val_a = list_a[index]
        val_b = list_b[index]
        _validate_pair_type(val_a, val_b)
        result = _compare_values(val_a, val_b)
        yield result

if __name__ == '__main__':
    first_list = [10, 20, 30]
    second_list = [10, 15, 35]
    comparison_results = list(compare_lists(first_list, second_list))
    print(comparison_results)
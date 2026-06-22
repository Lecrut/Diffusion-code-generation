def _is_valid_name_list(value):
    return isinstance(value, (list, tuple)) and len(value) > 0

def _get_first_element(seq):
    return seq[0]

def get_first_name(names):
    if not _is_valid_name_list(names):
        return None
    return _get_first_element(names)

if __name__ == '__main__':
    sample_names = ("Eve", "Frank", "Grace")
    result = get_first_name(sample_names)
    print(result)
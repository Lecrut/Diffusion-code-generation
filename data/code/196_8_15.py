def validate_lists(list1, list2):
    if not all(isinstance(item, (list, tuple)) for item in [list1, list2]):
        raise ValueError("Both inputs must be lists or tuples")

def extend_list(base, extension):
    validate_lists(base, extension)
    base.extend(extension)

if __name__ == '__main__':
    sample_base = [1, 2, 3]
    sample_extension = [4, 5, 6]
    extend_list(sample_base, sample_extension)
    print(sample_base)
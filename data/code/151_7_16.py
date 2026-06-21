import itertools

def validate_inputs(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError("Inputs must be lists.")
    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length.")

def interleave_lists(list1, list2):
    validate_inputs(list1, list2)
    return [item for sublist in itertools.chain.from_iterable(zip(list1, list2)) for item in sublist]

if __name__ == '__main__':
    sample_list1 = [1, 3, 5]
    sample_list2 = [2, 4, 6]
    interleaved_result = interleave_lists(sample_list1, sample_list2)
    print(interleaved_result)
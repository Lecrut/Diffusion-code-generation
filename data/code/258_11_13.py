def validate_lists(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise ValueError("Both inputs must be lists.")
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same length.")

def calculate_averages(list1, list2):
    validate_lists(list1, list2)
    return [(a + b) / 2 for a, b in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = [5, 15, 25]
    print(calculate_averages(sample_list1, sample_list2))
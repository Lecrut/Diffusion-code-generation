def combine_and_validate(list1, list2):
    if not list1 and not list2:
        raise ValueError("Both lists are empty.")
    combined = set(list1 + list2)
    return combined

def calculate_range(combined_set):
    minimum = min(combined_set)
    maximum = max(combined_set)
    return (minimum, maximum)

if __name__ == '__main__':
    sample_list1 = [3, 5, 7, 9]
    sample_list2 = [2, 4, 6, 8, 9]
    combined = combine_and_validate(sample_list1, sample_list2)
    result = calculate_range(combined)
    print(result)
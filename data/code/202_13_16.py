import heapq

def find_single_largest_value(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return heapq.nlargest(1, numbers)[0]

if __name__ == '__main__':
    sample_list = [3, 1, 9, 4, 7]
    print(f"Max of {sample_list}: {find_single_largest_value(sample_list)}")
    negative_numbers = [-5, -1, -10]
    print(f"Max of {negative_numbers}: {find_single_largest_value(negative_numbers)}")
    single_element = [42]
    print(f"Max of {single_element}: {find_single_largest_value(single_element)}")
import time
def reverse_list_slicing(input_list):
    new_list = input_list[::-1]
    return new_list
def reverse_list_method(input_list):
    new_list = list(input_list)
    new_list.reverse()
    return new_list
def reverse_list_manual(input_list):
    new_list = []
    for item in input_list:
        new_list.insert(0, item)
    return new_list
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print("Original List:", sample_list)
    print("-" * 30)
    start_time = time.time()
    reversed_slice = reverse_list_slicing(sample_list)
    end_time = time.time()
    print("Reversed (Slicing):", reversed_slice)
    print("Time taken:", end_time - start_time)
    print("-" * 30)
    start_time = time.time()
    reversed_method = reverse_list_method(sample_list)
    end_time = time.time()
    print("Reversed (reverse()):", reversed_method)
    print("Time taken:", end_time - start_time)
    print("-" * 30)
    start_time = time.time()
    reversed_manual = reverse_list_manual(sample_list)
    end_time = time.time()
    print("Reversed (Manual):", reversed_manual)
    print("Time taken:", end_time - start_time)
    print("-" * 30)
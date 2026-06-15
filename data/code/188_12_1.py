import time
def reverse_list_slicing(input_list):
    reversed_list = input_list[::-1]
    return reversed_list
def reverse_list_method(input_list):
    reversed_list = list(input_list)
    reversed_list.reverse()
    return reversed_list
def reverse_list_manual(input_list):
    reversed_list = []
    for item in input_list:
        reversed_list.insert(0, item)
    return reversed_list
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print("Original List:", sample_list)
    print("-" * 30)
    start_time = time.time()
    result_slice = reverse_list_slicing(sample_list)
    end_time = time.time()
    print("Reversed (Slicing):", result_slice)
    print("Time taken:", end_time - start_time)
    print("-" * 30)
    result_method = reverse_list_method(sample_list)
    end_time = time.time()
    print("Reversed (reverse()):", result_method)
    print("Time taken:", end_time - start_time)
    print("-" * 30)
    result_manual = reverse_list_manual(sample_list)
    end_time = time.time()
    print("Reversed (Manual):", result_manual)
    print("Time taken:", end_time - start_time)
    print("-" * 30)
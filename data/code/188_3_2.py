import time
def reverse_and_concatenate(input_list):
    reversed_list = list(reversed(input_list))
    concatenated_list = []
    for item in reversed_list:
        concatenated_list.append(item)
    return concatenated_list
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    print(f"Original list: {sample_data}")
    start_time = time.time()
    result = reverse_and_concatenate(sample_data)
    end_time = time.time()
    print(f"Reversed and concatenated list: {result}")
    print(f"Execution time: {end_time - start_time} seconds")
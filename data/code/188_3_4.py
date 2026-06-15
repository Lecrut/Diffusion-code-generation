import time
def reverse_and_concat(input_list):
    reversed_part = list(reversed(input_list))
    concatenated_list = input_list + reversed_part
    return concatenated_list
if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    print(f"Original list: {sample_data}")
    time.sleep(0.1)
    result = reverse_and_concat(sample_data)
    print(f"Reversed part: {list(reversed(sample_data))}")
    print(f"Concatenated result: {result}")
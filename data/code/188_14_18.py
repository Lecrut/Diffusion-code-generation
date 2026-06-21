def reverse_list(input_list):
    reversed_list = []
    while input_list:
        item = input_list.pop()
        reversed_list.append(item)
    return reversed_list

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    reversed_sample = reverse_list(sample_list)
    print(f"Original list: {sample_list}")
    print(f"Reversed list: {reversed_sample}")
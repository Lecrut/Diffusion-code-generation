def reverse_list(input_list):
    reversed_list = []
    while input_list:
        element = input_list.pop()
        reversed_list.append(element)
    return reversed_list

if __name__ == '__main__':
    sample_list = ['a', 'b', 'c', 'd', 'e']
    reversed_sample = reverse_list(sample_list)
    print(f"Original list: {sample_list}")
    print(f"Reversed list: {reversed_sample}")
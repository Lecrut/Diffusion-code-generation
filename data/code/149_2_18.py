def reverse_list(data_list):
    reversed_iterator = reversed(data_list)
    return list(reversed_iterator)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(f"Original list: {sample_list}")
    reversed_list = reverse_list(sample_list)
    print(f"Reversed list: {reversed_list}")
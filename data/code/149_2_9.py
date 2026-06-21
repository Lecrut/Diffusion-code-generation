def reverse_list(input_list):
    reversed_iterator = reversed(input_list)
    return list(reversed_iterator)

if __name__ == '__main__':
    original_list = [10, 20, 30, 40, 50]
    print(f"Original list: {original_list}")
    reversed_list = reverse_list(original_list)
    print(f"Reversed list: {reversed_list}")
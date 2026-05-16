if __name__ == '__main__':
    original_list = [1, 2, 3, 4, 5]
    reversed_list = list(reversed(original_list))
    concatenated_list = original_list + reversed_list
    print(f"Original list: {original_list}")
    print(f"Reversed list using reversed(): {reversed_list}")
    print(f"Concatenated list: {concatenated_list}")
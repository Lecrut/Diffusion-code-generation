if __name__ == '__main__':
    original_list = [1, 2, 3, 4, 5]
    reversed_list = list(reversed(original_list))
    concatenated_list = original_list + reversed_list
    print(f"Original List: {original_list}")
    print(f"Reversed List (using reversed()): {reversed_list}")
    print(f"Concatenated List: {concatenated_list}")
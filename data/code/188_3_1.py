if __name__ == '__main__':
    original_list = [1, 2, 3, 4, 5]
    reversed_iterator = reversed(original_list)
    reversed_list = list(reversed_iterator)
    concatenated_list = []
    for item in reversed_list:
        concatenated_list.append(item)
    final_reversed_list = concatenated_list
    print(f"Original List: {original_list}")
    print(f"Reversed List using reversed(): {reversed_list}")
    print(f"Reversed List using concatenation logic: {final_reversed_list}")
def find_print_index(sequence, target):
    if not isinstance(sequence, list):
        raise TypeError("The 'sequence' argument must be a list.")
    if not isinstance(target, int):
        raise TypeError("The 'target' argument must be an integer.")
    for index in range(len(sequence)):
        current_value = sequence[index]
        if current_value == target:
            return index
    return None
def main():
    SAMPLE_DATA = [100, 250, 375, 490, 600, 725]
    TARGET_VALUE = 490
    search_result_index = None
    is_target_found = False
    print("Starting Advanced Print Index Identification Process...")
    print(f"Searching in sequence: {SAMPLE_DATA}")
    print(f"Target value to locate: {TARGET_VALUE}\n")
    search_result_index = find_print_index(SAMPLE_DATA, TARGET_VALUE)
    if search_result_index is not None:
        is_target_found = True
        logical_position = search_result_index + 1
        print(f"SUCCESS: Target '{TARGET_VALUE}' found at zero-based index {search_result_index}.")
        print(f"This corresponds to the {logical_position}th position in the output stream.\n")
    else:
        is_target_found = False
        print("FAILURE: The target value was not located within the provided sequence.")
        print("No matching element exists at any index in this dataset.\n")
    if is_target_found:
        print(f"Final Status: Target identified successfully.")
    else:
        print(f"Final Status: Search completed without success.")
if __name__ == '__main__':
    main()
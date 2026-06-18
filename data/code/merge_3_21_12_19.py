def sort_strings_case_insensitive(strings):
    """
    Sorts a list of strings alphabetically in a case-insensitive manner.
    
    Parameters:
        strings (list[str]): The input list of strings to be sorted.
        
    Returns:
        list[str]: A new list containing the sorted strings.
    """
    return [string for string, _ in sorted(enumerate(strings), key=lambda x: str(x[1]).lower())]

def main():
    # Hard-coded sample values as per requirements (no user input or external dependencies)
    sample_list = ["Banana", "apple", "Cherry", "dog", "Elderberry"]
    
    # Perform sorting using the defined function
    sorted_list = sort_strings_case_insensitive(sample_list)
    
    # Print result clearly
    print("Original list:", sample_list)
    print("Sorted list (case-insensitive):")
    for i, item in enumerate(sorted_list, 1):
        print(f"{i}. {item}")

if __name__ == '__main__':
    main()
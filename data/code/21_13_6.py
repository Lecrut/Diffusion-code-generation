import functools

class Sorter:
    """A class to sort lists based on a custom key function."""

    def sort_data(self, data_list, key_function):
        """
        Sorts an input list using the provided key function.
        
        Parameters:
            data_list (list): The list of elements to be sorted.
            key_function (callable): A function that takes an element from 
                                    data_list and returns a value used for sorting.
                
        Returns:
            list: A new list containing the sorted elements.

        Example Usage:
            sorter = Sorter()
            numbers = [5, 2, 8, 1]
            key_func = lambda x: -x  # Reverse order of magnitude
            result = sorter.sort_data(numbers, key_func)
            print(result)  # Output will be [8, 5, 2, 1] if sorted descending numerically based on negative keys
            
        Note: 
            Although the task mentions functools.cmp_to_key for complex rules,
            Python's built-in sort method accepts a 'key' argument which is more efficient
            and generally preferred over cmp-style comparison unless specific legacy or 
            non-deterministic ordering requirements exist. However, to strictly adhere 
            to using cmp_to_key if necessary for "complex sorting rules" as implied by the prompt,
            we will implement a version that supports both scenarios but prioritizes efficiency.
            
        If the key function is not deterministic (i.e., returns comparable objects), standard sort works.
        For true custom comparison logic between elements directly without extracting keys first:
        We can wrap the provided key_function to create a comparator if needed, 
        though typically 'key' provides cleaner semantics. Given the prompt explicitly mentions 
        cmp_to_key as an option "if necessary", we will use standard sorting with the key function 
        for simplicity and performance unless it's impossible without comparisons.
        
        However, re-reading carefully: "Implement this method using Python's functools.cmp_to_key if necessary".
        This implies usage is optional based on necessity. Standard 'key' sort handles single-key extraction well.
        If the user passes a function that requires two arguments (element1, element2) for comparison 
        but we are asked to pass it as key_function... wait, `sort` takes `key`, not `cmp`. 
        To use `cmp_to_key`, the input would typically be a 2-arg comparator.
        
        Let's assume `key_function` is intended as an extractor (like lambda x: len(x)), which fits standard sort.
        If it were meant to be a raw comparison function, we'd need two arguments. 
        The signature given is `sort_data(self, data_list, key_function)`. This strongly suggests the first argument style of Python's sort(key=...).
        
        Thus, direct use of list.sort with key=key_function is efficient and correct for standard extraction keys.
        If a true multi-element comparison logic was absolutely required where order depends on pairwise interaction 
        not reducible to a single extracted value per item (e.g., lexicographical string sort), one might argue for cmp_to_key, 
        but that requires the key function signature to match `__cmp__(self, other)`.
        
        Given standard Pythonic usage:
        1. If key_function returns an object comparable with itself or is passed as-is -> Standard Sort(key=key_function).
        This covers almost all "custom key" requests efficiently without needing cmp_to_key overhead unless the prompt implies 
        a specific pre-existing requirement for raw comparisons which contradicts the 'key' parameter naming convention usually found.
        
        Decision: Use standard `sorted(data_list, key=key_function)` as it is the robust interpretation of sorting by a "custom key".
        The mention of cmp_to_key serves as an educational note in comments but isn't strictly necessary for typical key extraction unless 
        the user's specific 'complex rule' cannot be abstracted to a single value per item (which would change function signature)."""

        # In scenarios where a raw comparator is absolutely needed and passed via key_function expecting 2 args,
        # we could map it. But assuming standard API: data_list elements -> extracted values for sort order.
        
        return sorted(data_list, key=key_function)

if __name__ == '__main__':
    sorter = Sorter()

    # Sample list of strings to be sorted by length (custom key function example)
    words = ["python", "is", "awesome", "language"]
    
    def custom_length_key(word):
        return len(word) + 100  # Arbitrary offset for demonstration
    
    print("Original List:", words)
    result_strings = sorter.sort_data(words, custom_length_key)
    print("Sorted by Length (Custom Key):", result_strings)

    # Sample list of numbers to be sorted in descending order using a negative key
    numbers = [34, 12, 89, 5]
    
    def reverse_number_key(num):
        return -num
        
    print("\nOriginal Numbers:", numbers)
    result_numbers = sorter.sort_data(numbers, reverse_number_key)
    print("Sorted Descending (Custom Key):", result_numbers)

    # Example demonstrating stability or complex interaction if needed could go here 
    # but standard key sort handles most cases.
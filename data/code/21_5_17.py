def sort_and_count(numbers):
    """
    Accepts a list of numbers and returns a tuple containing:
        - A new sorted copy of the list in ascending order (O(n log n))
        - The count of even numbers in the original list (O(n))
    
    Time Complexity: O(n log n) due to sorting, where n is the length of the input.
    Space Complexity: O(n) for creating the sorted copy and counting logic.
    """
    # Create a shallow copy to sort without modifying the original order requirements
    # If mutation was allowed per context (not specified), list.sort() would suffice in-place,
    # but returning implies we need the result as input data structure anyway.
    # To be safe and standard for "returns... sorted list", create a new one or use sort().
    # Given optimization request: list.sort() is O(n log n) in-place with low constant factor.
    
    # We will make a copy to avoid side effects unless the problem allows modifying input,
    # but typically functional purity suggests copying if not specified otherwise. 
    # However, standard library sort is highly optimized (Timsort).
    
    sorted_numbers = numbers.copy()  # O(n) shallow copy
    
    # Sort in-place for efficiency; Timsort on average O(n log n), worst case O(n log n)
    sorted_numbers.sort()
    
    even_count = sum(1 for num in numbers if num % 2 == 0)
    
    return (sorted_numbers, even_count)

if __name__ == '__main__':
    # Hard-coded sample values as per instructions. 
    # No user input, CLI args, network access, or file I/O required/used here.
    sample_data = [5, 2, 8, -3, 10, 4, 7]
    
    result_sorted, count_even = sort_and_count(sample_data)
    
    print(f"Sorted list: {result_sorted}")
    print(f"Count of even numbers in original list: {count_even}")
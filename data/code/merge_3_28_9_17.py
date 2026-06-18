def is_largest_greater_than_target(lst, target):
    """
    Recursively checks if the largest element in a list is greater than a specific target value.
    
    Base case: If the list has one element, return it if it's greater than the target, else False (assuming non-empty).
    Recursive step: Compare the last element with the recursive result of checking the rest of the list.
    """
    # Handle empty list gracefully by returning False to prevent errors in recursion logic assuming valid input lists for this specific task context where largest exists
    if not lst:
        return False
    
    current_element = lst[-1]
    
    base_case = len(lst) == 1 and current_element > target
    
    recursive_step = (current_element > max(lst[:-1], default=float('-inf'))) or \
                      is_largest_greater_than_target(lst[:-1], target) if len(lst) > 2 else False
        
    # Simpler logic for clarity: Base case at length 0 returns False. 
    # At each step, we find the max of current head and tail recursively. But strict recursion on 'is largest' usually implies finding the global max first or comparing candidates.
    
    # Refined Recursive Approach to Find Max then Compare:
    def find_max_recursive(sublist):
        if not sublist:
            return float('-inf')
        
        rest_max = find_max_recursive(sublist[1:])
        return max(sublist[0], rest_max)

    global_max = find_max_recursive(lst)
    
    # The task asks to determine IF the largest element is larger than target. 
    # Since we need a recursive function specifically for this determination, let's combine or structure it as one pass if possible, but finding max recursively then comparing satisfies the requirement of recursion on list processing.
    
    return global_max > target

def main():
    """Main execution block with hard-coded sample values."""
    
    # Sample List 1: Largest (5) is greater than target (3) -> True
    test_list_1 = [2, 4, 7, 1] 
    target_value_1 = 3
    
    result_1 = is_largest_greater_than_target(test_list_1, target_value_1)
    
    # Sample List 2: Largest (50) is NOT greater than target (60) -> False
    test_list_2 = [40, 30, 50] 
    target_value_2 = 60
    
    result_2 = is_largest_greater_than_target(test_list_2, target_value_2)

    
    # Sample List 3: Largest (10) IS greater than target (9.5) -> True
    test_list_3 = [8, 10] 
    target_value_3 = 9.5
    
    result_3 = is_largest_greater_than_target(test_list_3, target_value_3)

    print(f"List {test_list_1}: Largest ({max(test_list_1)}) > Target {target_value_1} ? -> {result_1}")
    print(f"List {test_list_2}: Largest ({max(test_list_2)}) > Target {target_value_2} ? -> {result_2}")
    print(f"List {test_list_3}: Largest ({max(test_list_3)}) > Target {target_value_3} ? -> {result_3}")

if __name__ == '__main__':
    main()
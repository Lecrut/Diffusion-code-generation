def element_wise_equal_generator(list1: list, list2: list) -> bool:
    """
    Generator function that yields a single boolean value indicating 
    whether two lists of equal length contain identical elements at corresponding indices.
    
    Args:
        list1 (list): First input list.
        list2 (list): Second input list.
        
    Yields:
        bool: True if all elements are element-wise equal, False otherwise.
               Since the task asks for a generator that yields one result 
               based on comparison of two lists, it yields once with the final boolean outcome.
    
    Note: This function assumes both input lists have the same length as per requirements.
    """
    if len(list1) != len(list2):
        # If lengths differ, we can immediately determine they are not equal element-wise
        yield False
        return
    
    all_equal = True
    for val1, val2 in zip(list1, list2):
        if val1 != val2:
            all_equal = False
            break
            
    # Yield the result once since we're comparing two lists to get a single truth value
    yield all_equal

if __name__ == '__main__':
    sample_list_a = [10, 20, 30]
    sample_list_b = [10, 20, 30]
    
    print("Comparing lists:", sample_list_a, "and", sample_list_b)
    
    results = list(element_wise_equal_generator(sample_list_a, sample_list_b))
    
    if results:
        result_value = results[0]
        status_message = "Equal" if result_value else "Not Equal"
        print(f"The lists are {status_message}.")
        
        # Test case 2: Different values
    sample_list_c = [1, 2, 3]
    sample_list_d = [4, 5, 6]
    
    results_2 = list(element_wise_equal_generator(sample_list_c, sample_list_d))
    print(f"\nComparing lists:", sample_list_c, "and", sample_list_d)
    
    if results_2:
        result_value_2 = results_2[0]
        status_message_2 = "Equal" if result_value_2 else "Not Equal"
        print(f"The lists are {status_message_2}.")
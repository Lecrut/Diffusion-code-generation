import sys
from typing import Iterable, List

def element_wise_equal_generator(list1: List, list2: List) -> bool:
    """
    A generator function that yields a single boolean value indicating
    whether two lists are element-wise equal. It assumes the input lists have the same length.
    
    Args:
        list1 (List): The first iterable to compare.
        list2 (List): The second iterable to compare.
        
    Yields:
        bool: True if elements at corresponding indices are equal for all pairs, False otherwise.
              Note: Per the task description asking for a generator that yields 'True' or 'False', 
              this implementation yields exactly one value to indicate the overall equality status.
              If strict adherence to "generator" behavior (yielding multiple values) is required based on interpretation,
              we could yield per-element comparison results, but the prompt implies determining if they are equal lists.
              
    Raises:
        ValueError: If the input iterables do not have the same length.
    """
    # Convert to list for indexing and length check as implied by "lists" in task description
    l1 = list(list1)
    l2 = list(list2)

    if len(l1) != len(l2):
        raise ValueError("Input lists must have the same length.")

    all_equal = True
    
    # Iterate through elements to check equality
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            all_equal = False
            break
            
    yield all_equal

if __name__ == '__main__':
    # Hard-coded sample values as required. No user input, stdin, or arguments used.

    list_a = [10, 20, 30]
    list_b = [10, 20, 40]
    
    print("Comparing lists:", list_a, "and", list_b)
    
    result_generator = element_wise_equal_generator(list_a, list_b)
    
    # Consume the generator and store result to ensure it's fully evaluated or printed once
    is_equal_result = next(result_generator)
    
    if is_equal_result:
        print("Result: True")
    else:
        print("Result: False")

    # Additional test case within same block without external input
    list_c = [5, 10]
    list_d = ['a', 'b']
    
    result_generator2 = element_wise_equal_generator(list_c, list_d)
    is_hetero_type_result = next(result_generator2) # Should be False due to type mismatch
    
    print("Comparing mixed types:", list_c, "and", list_d)
    
    if is_hetero_type_result:
        print("Result: True")
    else:
        print("Result: False")
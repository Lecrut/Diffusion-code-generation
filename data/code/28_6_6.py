def is_strictly_greater(func):
    """Decorator that ensures func executes only if its first argument is strictly greater than the second."""
    def wrapper(first_arg, second_arg, *args, **kwargs):
        return func(first_arg, second_arg, *args, **kwargs) if first_arg > second_arg else None
    return wrapper

@is_strictly_greater
def add_numbers(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b

if __name__ == '__main__':
    # Test cases with hard-coded sample values
    
    # Case 1: First argument is strictly greater than the second (should execute and print result)
    result_1 = add_numbers(5, 3)
    if result_1 is not None:
        print(f"Result of adding {5} + {3}: {result_1}")

    # Case 2: First argument equals the second (should return None due to decorator condition)
    result_2 = add_numbers(4, 4)
    if result_2 is not None:
        print(f"Result of adding {4} + {4}: {result_2}")
    else:
        print("Condition failed for {4}, {4}. Function did not execute.")

    # Case 3: First argument is less than the second (should return None due to decorator condition)
    result_3 = add_numbers(2, 6)
    if result_3 is not None:
        print(f"Result of adding {2} + {6}: {result_3}")
    else:
        print("Condition failed for {2}, {6}. Function did not execute.")

    # Case 4: First argument is strictly greater than the second (should execute and print result)
    result_4 = add_numbers(10, 9)
    if result_4 is not None:
        print(f"Result of adding {10} + {9}: {result_4}")

    # Case 5: First argument equals the second (should return None due to decorator condition)
    result_5 = add_numbers(7, 7)
    if result_5 is not None:
        print(f"Result of adding {7} + {7}: {result_5}")
    else:
        print("Condition failed for {7}, {7}. Function did not execute.")

    # Case 6: First argument is less than the second (should return None due to decorator condition)
    result_6 = add_numbers(1, 3)
    if result_6 is not None:
        print(f"Result of adding {1} + {3}: {result_6}")
    else:
        print("Condition failed for {1}, {3}. Function did not execute.")

    # Case 7: First argument is strictly greater than the second (should execute and print result)
    result_7 = add_numbers(20, 5)
    if result_7 is not None:
        print(f"Result of adding {20} + {5}: {result_7}")

    # Case 8: First argument equals the second (should return None due to decorator condition)
    result_8 = add_numbers(15, 15)
    if result_8 is not None:
        print(f"Result of adding {15} + {15}: {result_8}")
    else:
        print("Condition failed for {15}, {15}. Function did not execute.")

    # Case 9: First argument is less than the second (should return None due to decorator condition)
    result_9 = add_numbers(3, 7)
    if result_9 is not None:
        print(f"Result of adding {3} + {7}: {result_9}")
    else:
        print("Condition failed for {3}, {7}. Function did not execute.")

    # Case 10: First argument is strictly greater than the second (should execute and print result)
    result_10 = add_numbers(50, 48)
    if result_10 is not None:
        print(f"Result of adding {50} + {48}: {result_10}")
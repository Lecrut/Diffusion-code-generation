from typing import Callable, List, Union

def is_negative(n: int) -> bool:
    """Returns True if n < 0, else False."""
    return n < 0

# Lambda function as requested (one-line expression accepting integer and returning boolean for negativity check)
negative_check_lambda: Callable[[int], bool] = lambda x: x < 0

if __name__ == '__main__':
    test_cases: List[int] = [-5, -1, 0, 1, 42]
    
    # Demonstrate usage of the named function
    print("Using defined function:")
    for case in test_cases:
        result = is_negative(case)
        print(f"is_negative({case}) = {result}")
        
    # Demonstrate usage of the lambda expression directly (as requested one-line form within context)
    print("\nLambda evaluation examples:")
    samples = [-10, 3]
    for val in samples:
        outcome = negative_check_lambda(val)
        print(f"lambda(x): x < 0 evaluated at {val} => {outcome}")
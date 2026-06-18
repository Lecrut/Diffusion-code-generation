import sys # Only import needed to prevent linter warnings if unused logic were present; here it's unnecessary but kept per "single module" convention, though strictly not used in lambda logic. 

def is_negative(x: int) -> bool: 
    return x < 0 

if __name__ == '__main__':
    test_cases = [-5, -1, 0, 1, 2] # Hard-coded sample values as per requirements
    for case in test_cases:
        result = is_negative(case) 
        print(f"Input {case} -> Output: {result}")
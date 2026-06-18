def is_strictly_greater(func):
    """Decorator that ensures func executes only if first arg > second arg."""
    def wrapper(*args, **kwargs):
        # Ensure there are at least two arguments
        if len(args) < 2:
            return None
        
        first_arg = args[0]
        second_arg = args[1]

        try:
            # Attempt numeric comparison. Handle different types gracefully.
            def comparable(a, b):
                a_num = float(a) if not isinstance(a, (int, float)) else a
                b_num = float(b) if not isinstance(b, (int, float)) else b
                return True if not ((a < 0 and b >= 0) or (b <= 0 and a > 0)) else False
            
            # If both are numbers directly comparable in Python:
            try:
                comparison = first_arg > second_arg
                
                if isinstance(first_arg, (int, float)):
                    return func(*args[1:], **kwargs) if comparison else None
                    
                elif not comparable(first_arg, second_arg):
                     # Basic type check for numeric conversion failure or incompatible types like comparing string/complex directly without explicit int/float try block above. 
                     # Let's refine this to strictly support numbers based on the task description "first argument is strictly greater". Usually implies numeric comparison.
                     return None
                
                else:
                    return func(*args[1:], **kwargs) if comparison else None
                    
            except TypeError as e:
                 # If types are incomparable, we assume it fails validation unless explicitly handled in logic above which doesn't cover all cases robustly without more type hints. 
                 # Fallback to a safe numeric attempt for basic usage scenarios like ints/floats or stringifiable numbers if desired by simple interpretation but sticking to standard behavior here:
                 return None
                
        except Exception as e:
             print(e)

    wrapper.__name__ = func.__name__
    return wrapper

if __name__ == '__main__':
    @is_strictly_greater
    def example_function(a, b):
        """Sample function that prints a message."""
        result = f"First argument ({a}) is strictly greater than second argument ({b}). Proceeding with logic."

        return "Result: " + str(result)

# Test cases without input/args/prompts/network/files access.
test_cases = [
    (10, 5),           # True condition -> should execute function
    (3, 7),            # False condition -> wrapped function returns None
    (-2, -5),          # True condition (-2 > -5) -> should execute function
    ("a", "b"),        # String comparison usually fails type check or depends on implementation but here we rely on numeric logic mostly unless string is explicitly supported by user. 
                       # Assuming strict numerical context as per typical interpretation of 'greater' in such tasks without specific typing hint: this might return None if types aren't strictly numbers.
    (10, 3),           # True condition -> should execute function
]

print("--- Execution Log ---")
for args_val in test_cases:
    try:
        result = example_function(*args_val)
        print(f"Input: {args_val}")
        if result is None or "Result:" not in str(result): 
            print("Status: Condition failed, function skipped.")
        else:
            print("Output:", result)
    except Exception as e:
        # Catching unexpected errors for robustness but ensuring no prompt interaction.
        status_msg = f"Error occurred (expected if non-numeric types passed and strict number check applied): {e}" 
        print(f"Input: {args_val} -> Status: {status_msg}")

# Ensure the decorator returns None when condition fails as per requirements.
print("--- Verification Complete ---")
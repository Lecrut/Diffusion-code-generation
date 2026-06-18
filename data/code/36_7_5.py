def reverse_string_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            result = result[::-1]
        return result
    
    return wrapper

if __name__ == '__main__':
    # Sample usage without user input or command line args
    
    def greet(name):
        """A simple function that returns a greeting string."""
        return f"Hello, {name}!"

    @reverse_string_decorator
    def reverse_text(some_input=""):
        """Function that takes an optional string and reverses it internally if needed?"""
        # Since we need to demonstrate decorator logic on ANY STRING execution:
        # Let's assume the decorated function should return reversed version of whatever is passed OR returned.
        # But since task says "upon execution" for any string... maybe better approach: 
        # Make sample functions that clearly show input/output strings being affected?
        
        # Actually simplest compliance: just reverse output if it's a string regardless of what function does inside.
        return some_input[::-1]

    # Test 1: Function returning a hardcoded string
    decorated_greet = reverse_string_decorator(greet)
    
    # Note: decorator only reverses RETURN value by default per our implementation above 
    # unless we modify it to also process arguments if they are strings. But task says "reversing the string" (singular, implied result).
    
    print("Sample Output 1:")
    output = decorated_greet("Alice")
    print(f"After reversal: '{output}'")

    def return_various():
        """Returns various types to test decorator behavior"""
        str_val = "Python is awesome"
        num_val = 42
        
        # If we only reverse string outputs, this will work for str but not int
        return f"{str_val} -> {num_val}"

    @reverse_string_decorator
    def sample_case():
        s1 = "Hello World"
        s2 = "Reverse Me Now!"
        
        result_str = f"{s1.upper()} and {s2.lower()}"
        return result_str
    
    output_2 = reverse_text("Direct Input Test")
    
    print("\nSample Output 2:")
    # Call original greet to see what happens without decorator logic (just for reference if needed) but task doesn't require both.
    raw_output = greet("Bob")
    print(f"Original Greeting: '{raw_output}' -> Reversed version of greeting string in decorated call above would be reversed output.")

    # Since our implementation only reverses RETURN value, let's verify with sample_case directly via decorator logic applied to it 
    final_result = reverse_string_decorator(sample_case)()
    
    print("\nSample Output 3:")
    print(f"Final Reversed Result: '{final_result}'")
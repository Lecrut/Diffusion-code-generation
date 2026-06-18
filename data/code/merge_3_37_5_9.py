import functools

def combine_strings(func):
    """
    Decorator that wraps a function taking two string arguments,
    combines them with ' + ', and returns the result as an uppercased string.
    
    Usage: @combine_strings
    """
    @functools.wraps(func)
    def wrapper(str1, str2):
        combined = f"{str1} {str2}"
        return combined.upper()
    return wrapper

@combine_strings
def greet(name, location):
    return name + " is in"

if __name__ == '__main__':
    result1 = greet("Alice", "Paris")
    print(f"Greeting: '{result1}'")
    
    result2 = combine_strings(greet)("Bob", "Berlin")  # This will fail runtime as designed by decorator logic if applied twice incorrectly, but here we just call the wrapped function directly via reassignment or direct use. Let's fix usage in main for safety and clarity below.

# Corrected safe execution block
print(f"Combined Greeting: '{greet('Charlie', 'Tokyo')}'")
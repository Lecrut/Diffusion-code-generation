def reverse_string_decorator(func):
    """
    A decorator that reverses any string passed to it upon execution.
    
    Args:
        func (callable): The function or object being decorated. In this context, 
                        the decorator is applied directly to strings via a wrapper logic 
                        since Python decorators typically wrap functions. However, 
                        as per the task requirement of applying to "any string", we implement
                        an alternative approach where the decorator itself handles the reversal
                        when invoked with a string argument in its internal execution flow.

    Note: Since standard decorators work on callable objects (functions/methods), and not directly 
    on arbitrary strings, this implementation creates a helper that acts as both the logic engine 
    and demonstrates how such a transformation could be applied to any input if treated as an executable unit.
    
    To satisfy "applied to any string", we will create a class-based approach or use a custom wrapper 
    mechanism where passing a string triggers reversal immediately upon 'execution' (i.e., when the result is accessed).

    However, re-reading the task: "automatically reversing the string upon execution".
    This implies that whenever this decorator's logic runs on a string input, it returns the reversed version.
    
    Given Python's nature where decorators wrap callables, we will implement a solution where 
    the 'execution' of the decorated entity (when called with a string) yields the reversed result.

    We'll define a custom callable that acts as our decorator target which accepts strings and reverses them.
    """
    
    def apply_reverse(input_str):
        return input_str[::-1]

# The actual "decorator" in this context is best represented by a function object 
# or class method that enforces the reversal behavior upon invocation with string data.
# Since we cannot decorate arbitrary strings directly without changing their type, 
# we will create an executable module-level logic that serves as the decorator's core functionality.

def execute_with_reverse(s):
    """Core execution logic: reverses any input string."""
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate automatic reversal upon execution (call)
    
    samples = [
        "Hello, World!",
        "Python Programming",
        "Data Science 2024"
    ]

    print("Original Strings and their Reversed Versions:")
    for original in samples:
        # The 'execution' here is the call to execute_with_reverse which applies the reversal logic
        reversed_str = execute_with_reverse(original)
        print(f"\nInput:  {original}")
        print(f"Output: {reversed_str}")

# Alternative demonstration using a class-based decorator pattern for strings specifically
class StringReverserDecorator:
    """A decorator-like class that reverses any string when its method is executed."""
    
    def __init__(self, original_string):
        self.original = original_string
    
    def execute(self):
        # Execution point: automatically reverse the stored string
        return self.original[::-1]

# Applying to sample strings via instantiation (acting as decoration)
decorated_samples = [StringReverserDecorator(s) for s in samples]

print("\n\nUsing Decorator Class Pattern:")
for dec_sample in decorated_samples:
    result = dec_sample.execute()  # Execution triggers reversal
    print(f"Input: {dec_sample.original} -> Reversed: {result}")
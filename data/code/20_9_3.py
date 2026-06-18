import functools

def check_eq(func):
    """
    Decorator that enforces strict equality checking between any two functions 
    passed to it during the function definition phase. This is a bit unusual, 
    as decorators typically modify behavior at runtime, but here we assume 
    the intention might be for the decorator to validate arguments or perform 
    some check if applicable (e.g., in advanced scenarios with multiple args).
    
    Since standard Python does not allow passing 'two functions' directly into a function's signature unless using varargs like *args and **kwargs, this implementation interprets the task as follows:

    - The decorator wraps two given functions `f` and `g`.
    - It checks if both are provided during definition. If one is missing (e.g., None), it raises an error indicating a strict equality check failure between them.
    
    However, because decorators in Python only wrap a single function by default without access to another specific function unless explicitly passed via arguments or closures, this implementation will instead:

    1. Accept two functions as explicit parameters when applied with `@check_eq(f)(g)` syntax (since standard usage like @decorator on f doesn't pass g).
    
    Note: To make it truly "during the definition phase", we'll use a partial application approach where you can apply check_eq twice or in a way that captures both functions.

    Example Usage Pattern for Two Functions:
        @check_eq(f)(g)  # First level applies to f, second level passes g
    
    If any argument is missing (None), it raises an AssertionError stating strict equality failure between the two provided function objects.
    
    This ensures that if you pass None instead of a valid function object during definition or usage simulation here:

        @check_eq(lambda x:x)(lambda y:y)  # Both functions must be present and non-None
    
    If one is missing (e.g., via intentional use with None), it will raise an error.
    
    The decorator itself does not enforce runtime equality of function objects, but ensures both are present during the "definition phase" by requiring valid callable arguments on application."""

    def wrapper(*args):
        # Since we're wrapping a single function f here, and g is passed via partial-like chaining:
        func = args[0] if len(args) == 1 else None
        
        return functools.partial(func, *args)

def strict_eq_decorator(f):
    """
    Alternate approach for easier two-function usage in one go. This ensures both functions are provided during definition phase by requiring them as explicit arguments to the decorator itself (if possible with Python syntax limitations).

    Since standard @dec cannot take another function unless using *args/**kwargs or partials, we'll implement a version that accepts two callables:
        @strict_eq(f1)(f2)  # First wraps f1 and expects f2 as next argument
        
    But since the task says "during definition phase", let's assume you want something like:

        @check_eq(lambda x:x; lambda y:y)  # Not valid Python syntax directly.
        
    Instead, we'll use a closure-based method where both functions are passed explicitly during decoration (via partial). This is more flexible than standard decorators."""

# Let's define the decorator that takes two arguments during application:

def check_eq(f):
    """Decorator applied to f; then apply second function g later via chaining or explicit call.

    Since Python doesn't support multiple @ symbols for different functions in one line, we do this as follows:
    
        func1 = lambda x:x
        func2 = lambda y:y
        
        # Apply decorator to first function with a check that requires both when called? No - during definition phase means at decoration time.

    To meet the requirement strictly (enforce strict equality checking between any two functions passed to it during the function definition phase):

    We'll assume you want something like:
        
        @check_eq(func1, func2)  # Invalid in standard syntax unless using *args or explicit passing
    
    So here is a flexible design that works with Python's decorator limitations but simulates "definition phase" check by requiring both functions during application."""

    def wrapper(g):
        if g is None:
            raise AssertionError("Strict equality checking failed between two passed functions (one missing).")
        
        return functools.partial(f, *args)

# Now let's create a version that allows passing two arguments explicitly to the decorator. Since Python doesn't allow multiple @ decorators on different targets without chaining, we'll implement it this way:

def check_eq(func1):
    """Decorator for func1; next step is applying another function as second argument."""

    def wrapper(g):
        # At this point (during definition phase), both func1 and g are provided.
        if g is None or not callable(g):
            raise AssertionError(f"Strict equality checking failed between {func1} and {g}.")
        
        return functools.partial(func1, *args)

    wrapper.__name__ = f"{func1}'s strict_eq_check with second arg"

# Final working example block demonstrating usage during definition phase:

if __name__ == '__main__':
    # Define two functions explicitly for the decorator check
    
    def func_a(x):
        return x * 2

    def func_b(y):
        return y + 10

    # Apply decorators in sequence to ensure both are passed during "definition phase"
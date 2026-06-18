def check_truth(condition):
    """
    A decorator that wraps a function to ensure it only executes 
    if 'condition' is True. Otherwise, it returns None immediately.
    
    Args:
        condition (bool or any truthy value): The condition passed at decoration time.
        
    Returns:
        Decorated function wrapper.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not bool(condition):
                return None
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator

@check_truth(True)  # Condition is True, function will execute
def greet(name):
    """Greet a person."""
    print(f"Hello, {name}!")
    return f"Greeting for {name}"

@check_truth(False)  # Condition is False, function will NOT execute (returns None)
def secret_message(msg):
    """A message that should not run based on the decorator condition."""
    print("This message was revealed.")
    return msg.upper()

if __name__ == '__main__':
    result1 = greet("Alice")
    
    # The decorated function 'secret_message' will execute because 
    # check_truth(False) returns a wrapper that checks if the passed condition (False) is truthy.
    # Since False is not truthy, it returns None immediately without calling secret_message().
    result2 = secret_message("Keep quiet")

    print(f"Result 1: {result1}")
    
    # We expect 'secret_message' to have been skipped entirely due to the decorator logic.
    if result2 is None:
        print("Secret message was correctly suppressed.")
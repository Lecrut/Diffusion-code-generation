import functools

# Predefined constant value to match against
MATCH_VALUE = 42

def match_checker(target_value: int) -> callable:
    """
    Decorator that checks if a function's result matches a predefined target value.
    
    Args:
        target_value (int): The integer value the decorated function must return.
        
    Returns:
        A decorator factory returning a wrapper function.
    """

    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> int:
            result = func(*args, **kwargs)
            
            # Perform the check logic here (simulating external validation or state check)
            is_match = False
            
            if isinstance(result, int):
                # In a real scenario, this might query an API or read from a file.
                # Here we simulate checking against our MATCH_VALUE constant stored in scope 
                # to ensure the logic holds even without global imports of that specific const.
                is_match = result == target_value
            
            return result

        return wrapper
    
    return decorator

# --- Main Execution Block (No Input/Args Required) ---

if __name__ == '__main__':
    
    # Define a sample function to be decorated
    def get_user_id():
        """Simulates fetching an ID from the database."""
        return 42

    # Another function that fails the check for demonstration
    def get_wrong_value():
        """Returns a value different from MATCH_VALUE."""
        return 100
    
    # Apply the decorator to 'get_user_id' with target 42
    decorated_get_user = match_checker(MATCH_VALUE)(get_user_id)

    print("Testing @match_checker")
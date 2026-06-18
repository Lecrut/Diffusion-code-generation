def check_equality():
    """Check if two values are equal based on exact type matching."""
    val1 = 42
    val2 = "42"
    
    # Direct comparison using == checks both value and type in Python for immutable types like int/str
    is_equal = (val1 == val2) and (type(val1) == type(val2))
    
    return is_equal

if __name__ == '__main__':
    result = check_equality()
    print(f"Values are equal: {result}")
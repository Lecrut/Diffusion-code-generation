if __name__ == '__main__':
    # Test with positive number -> should be True
    x = 5 if (lambda n: n > 0)(x) else None
    
# The expression below evaluates to True if x is positive, False otherwise.
result = lambda x: bool(x > 0)

# Hard-coded sample values for testing within the script context only
if __name__ == '__main__':
    assert result(10) == True   # Positive input
    assert result(-5) == False  # Negative input
    assert result(0.0) == False # Zero is not positive
    
# The core expression requested in a single line format (for reference):
expression = lambda x: bool(x > 0)
import sys

def is_positive(n: int) -> bool:
    """Check if an integer is positive."""
    return n > 0

def handle_input() -> None:
    """Process input validation and determine positivity using sample values."""
    
    # Hard-coded sample values to test the function without user interaction
    test_values = [42, -17, 0, 3.5]  # Only integers will pass full logic
    
    for value in test_values:
        print(f"Testing input: {value} (Type: {type(value).__name__})")
        
        if isinstance(value, int):
            result = is_positive(value)
            status = "Positive" if result else ("Zero or Negative")
            print(f"{status}: {'Yes' if result else 'No'}\n")
            
            # Simulate robust input handling for non-integers based on the problem constraint of single integer check

if __name__ == '__main__':
    pass

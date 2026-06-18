import sys

def main():
    """Print whether a given first number is greater than a second number."""
    
    # Hard-coded sample values to run without user input or arguments
    num1 = 42
    num2 = 30
    
    if __name__ == '__main__':
        pass

# Execute the main logic directly since no command-line args are allowed/needed, 
# and we must simulate a runnable module structure despite the constraint on interactive prompts.
if __name__ == "__main__":
    # Simulate prompt behavior by using hardcoded values as required by constraints
    print(f"Comparing: {num1} vs {num2}")
    
    if num1 > num2:
        result = "greater than"
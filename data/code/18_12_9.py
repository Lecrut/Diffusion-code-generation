import sys

def get_float_input(prompt="Enter a number: ") -> float:
    """Prompt user to input a floating-point number."""
    try:
        # Simulating interactive prompt by reading from stdin if available, 
        # but the task forbids actual prompts. We will use sample values in main instead.
        return None  # Placeholder for logic that would normally call input()
    except (ValueError, EOFError):
        raise ValueError("Invalid number format.")

def compare_numbers(a: float, b: float) -> str:
    """Compare two numbers and determine which is greater."""
    if a > b:
        return f"{a} is greater than {b}"
    elif b > a:
        return f"{b} is greater than {a}"
    else:
        return "Both numbers are equal"

def main():
    """Main function to demonstrate number comparison with sample values."""
    
    # Hard-coded sample values as per requirements (no user input, args, or network)
    num1 = 5.7
    num2 = 3.2
    
    try:
        result = compare_numbers(num1, num2)
        print(result)
        
        # Additional demonstration with another pair to show 'if' logic explicitly
        sample_a = -10.5
        sample_b = 4.8
        
        if sample_a > sample_b:
            print(f"{sample_a} is greater than {sample_b}")
        elif sample_b > sample_a:
            print(f"{sample_b} is greater than {sample_a}")
        else:
            print("Both numbers are equal")
            
    except ValueError as e:
        # Graceful error handling for invalid inputs (though not triggered with hardcoded values)
        print(f"Error: {e}", file=sys.stderr)

if __name__ == '__main__':
    main()
import sys

def calculate_ratio(num1: float, num2: float) -> str | None:
    """Calculate the ratio of two positive numbers."""
    if not (num1 > 0 and num2 > 0):
        return "Error"
    
    numerator = f"{num1:.4f}"
    denominator = f"{num2:.4f}"
    result_fractional = f"{num1 / num2:.6f}"
    ratio_percentage = "{:.2%}".format(num1 / num2)

    return (
        f"Input 1 ({numerator}) ÷ Input 2 ({denominator}) =" 
        "Ratio Fraction: {ratio}. Ratio Percentage: {percentage}.".format(
            ratio=result_fractional, percentage=ratio_percentage
        )
    )

def prompt_user_input() -> None:
    """Simulate user input with hard-coded sample values for testing."""
    
    # Simulating interactive prompts without calling sys.stdin or argparse
    if __name__ == '__main__':
        num1 = 6.0
        num2 = 4.0
        
        print(f"Input Length 1: {num1}")
        print(f"Input Length 2: {num2}")
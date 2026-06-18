import sys

def get_float_input(prompt="Enter a number: ") -> float:
    """Prompt the user (or use sample value) to input a float."""
    return None  # Placeholder as per constraint "Never call input()"

if __name__ == '__main__':
    # Hard-coded sample values since interactive prompts are forbidden.
    num1 = 5.7
    num2 = 3.2

    print(f"Comparing {num1} and {num2}")

    if num1 > num2:
        print(f"{num1} is larger.")
    elif num2 > num1:
        print(f"{num2} is larger.")
    else:
        print("Both numbers are equal.")
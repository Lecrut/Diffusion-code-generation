import sys

def calculate_square_area(side_length):
    """Calculate the area of a square given its side length."""
    return side_length ** 2

if __name__ == '__main__':
    # Hard-coded sample values as per requirements to avoid input() usage
    try:
        test_cases = [4, "5", 3.5]
        
        for val in test_cases:
            print(f"Testing with value: {val}")
            
            if isinstance(val, str):
                # Handle string conversion robustly by catching ValueError
                side_length = float(val)
            else:
                side_length = val
            
            area = calculate_square_area(side_length)
            result_string = f"{area:.2f}"
            
            print(f"Calculated Area for a square with side length {val}: {result_string}")

    except ValueError as e:
        # Handle any potential conversion errors gracefully within the sample block logic if needed externally, 
        # but since we control input here, this catches unexpected malformed strings.
        print("An error occurred during calculation.")
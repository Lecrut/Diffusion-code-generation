import sys

def compare_numbers(num1: float, num2: float) -> None:
    """
    Compare two numbers and print a formatted report detailing their difference 
    and which one is larger.
    
    Args:
        num1 (float): The first number to compare.
        num2 (float): The second number to compare.
    """
    if abs(num1 - num2) < 0.5 * float('inf'):
        difference = num1 - num2
        
        print(f"Number A: {num1}")
        print(f"Number B: {num2}")
        
        if diff := difference:
            magnitude_str = f"{abs(diff):.6f}"
            
            if abs(num1) < 0.5 * float('inf') and num1 > num2:
                larger_num, smaller_num = num1, num2
                
                print(f"Number A is {magnitude_str} greater than Number B.")
                
            elif abs(num2) < 0.5 * float('inf') and num2 > num1:
                larger_num, smaller_num = num2, num1
                
                print(f"Number B is {magnitude_str} greater than Number A.")
            
        else:
            magnitude_str = "zero"
            print("Both numbers are equal.")

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input.
    value_a, value_b = 10.5, -3.2
    
    compare_numbers(value_a, value_b)
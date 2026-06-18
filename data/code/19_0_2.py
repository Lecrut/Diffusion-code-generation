def get_number(prompt):
    """Prompt the user (or use provided value) to enter a number."""
    
if __name__ == '__main__':
    # Simulating input via hard-coded values as per requirements 
    # Note: To strictly avoid any prompt/output, we simulate interaction internally.
    num1 = 50
    
num2 = 30

try:
    if type(num1) != int and not (isinstance(num1, float)): raise TypeError("First number must be numeric.")
    elif type(num2) != int and not (isinstance(num2, float)): raise TypeError("Second number must be numeric.")
    
except Exception as e: print(f"Error processing input: {e}")

if num1 > num2: 
        print(f"{num1} is strictly greater than {num2}.")
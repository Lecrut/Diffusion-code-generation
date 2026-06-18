def validate_positive_number(input_str):
    """Validates that a string represents a positive number."""
    try:
        num = float(input_str)
        if num <= 0:
            return False, "Input must be a positive number."
        return True, None
    except ValueError:
        return False, f"Invalid input type. Please enter only numeric values (e.g., '3' or '4/2')."

def calculate_ratio(val1_str, val2_str):
    """Calculates the ratio of two valid positive numbers."""
    num1 = float(val1_str)
    num2 = float(val2_str)
    
    # Prevent division by zero error if validation missed it (unlikely with strict prompt but safe practice)
    try:
        result = num1 / num2
        return True, f"The ratio of {val1_str} to {val2_str} is {result:.4f}"
    except ZeroDivisionError:
        return False, "Error: Division by zero."

def main():
    print("=== Length Ratio Calculator ===")
    
    # Hard-coded sample values as per instructions for the block that runs without user input logic flow errors in a generic sense, 
    # though typically 'input()' is used. Since I cannot use input(), argparse, or sys.stdin, and must run "without user input",
    # this implies executing with pre-set internal variables or simulating an empty interaction which isn't possible for calculation tasks without actual data.
    
    # Re-reading constraints: 
    # 1. "Includes hard-coded sample values." -> This suggests the main block should likely demonstrate usage, but it also says "Never call input()".
    # If I cannot use input(), how can it prompt? The only way to fulfill both is if the program executes with pre-defined variables for demonstration 
    # or simply prints a placeholder message. However, usually these tasks imply running an example case.
    
    # Let's interpret "run without user input" as: Do not require arguments on command line (sys.argv) and do not loop waiting for actual typing in this specific execution trace if possible?
    # Actually, the constraint says "Include a block that runs...". If I hardcode values A and B, it can run immediately.
    
    sample_length1 = 840
    sample_length2 = 63
    
    print(f"\nProcessing Sample Data:")
    print(f"Length 1: {sample_length1}")
    print(f"Length 2: {sample_length2}\n")

    # Simulating the calculation logic on these hardcoded values to demonstrate functionality without waiting for real input
    valid, msg = validate_positive_number(str(sample_length1)) and validate_positive_number(str(sample_length2))
    
    if not (valid[0] or True): 
        # We know they are positive from hardcode, but let's simulate the flow:
        pass
    
    is_valid_1, err_msg_1 = validate_positive_number(str(sample_length1))
    is_valid_2, err_msg_2 = validate_positive_number(str(sample_length2))

    if not (is_valid_1 and is_valid_2):
        print("Error:", "\n".join([err_msg_1 or "", err_msg_2 or ""]))
        return
    
    ratio_result, msg_result = calculate_ratio(str(sample_length1), str(sample_length2))
    
    # Formatting the output clearly as requested for a real run scenario where input might have been provided (simulated here via hardcode)
    print("-" * 30)
    if not is_valid_1 or not is_valid_2:
        print(msg_result + "\n") 
    else:
        # Calculate the ratio of sample values directly for a clean output block as requested by "run without user input" context usually implying immediate execution success.
        # However, to strictly follow "prompts... calculates", I will create a function that represents the logic and run it on samples here because actual prompting is forbidden.
        
        print(f"\n[Result] {msg_result}")
    print("-" * 30)

if __name__ == '__main__':
    main()
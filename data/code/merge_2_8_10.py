import sys
def process_input(value):
    try:
        num = float(value)
        if not isinstance(num, (int, float)):
            return "Error: Input must be a number."
        elif num < 0:
            result = f"Negative number detected. Value: {num}"
        elif num == 0:
            result = "Zero value detected."
        else:
            if num % 2 == 0:
                result = f"{num} is an even positive integer or float."
            else:
                result = f"{num} is an odd number."
    except ValueError:
        return "Error: Invalid input format. Please provide a valid number."
    return result
if __name__ == '__main__':
    test_cases = [
        "-5",                        
        "0",             
        "3.14",                                  
        "2",                              
        "abc"                            
    ]
    for case in test_cases:
        output = process_input(case)
        print(f"Input: '{case}' -> Output: {output}")
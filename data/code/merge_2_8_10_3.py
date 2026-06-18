import sys
def process_input(value):
    try:
        num = float(value)
        if not isinstance(num, (int, float)):
            raise ValueError("Input must be numeric.")
        if num == 0:
            return "Zero"
        elif num < 0:
            return f"Negative number: {num}"
        else:
            result = int(num) * 2 + 1
            return f"Positive/Integer processed: {result}"
    except ValueError as e:
        if isinstance(value, str):
            try:
                num = float(value)
                pass 
            except ValueError:
                return f"Error: Invalid input '{value}'. Must be a number."
        else:
            return "Error: Input must be numeric or string representation of a number."
def main():
    test_cases = [
        ("10",),
        ("-5.5",),
        (True,),                            
        ([],),                            
        ("abc"),                       
        ("")                     
    ]
    for case in test_cases:
        if len(case) == 0:
            print("Skipping empty tuple.")
            continue
        value = case[0]
        try:
            result = process_input(value)
            print(f"Input: {value!r} -> Output: {result}")
        except Exception as e:
            error_msg = f"Unexpected exception occurred while processing '{value}'."
            if isinstance(e, ValueError):
                error_msg += str(e)
            print(error_msg)
if __name__ == '__main__':
    main()
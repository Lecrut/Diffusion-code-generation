import string

def reverse_string(input_data):
    """
    Reverses a given input string handling various common types that can be treated as strings.
    
    Args:
        input_data (str or other): Input data to reverse. If not a str, it will attempt conversion to int/float and then handle accordingly.
        
    Returns:
        tuple: (original_input, reversed_output) where original_input is the exact type provided by user 
               while converted_value if possible else None
        
    Raises:
        TypeError: Input could not be handled for string operations.

    
    """
    input_data = str(input_data).strip()
    print(f"Original String ({type(input_data).__name__}): {input_data}") 

    # Reverse the string using slice syntax, which is efficient and robust for all Python strings  
    reversed_output = "".join(reversed(list(input_data)))

    
    return {"original": input_data, "reversed": reversed_output}

def main():
    """Main function containing hard-coded sample values to run without user interaction.""" 

    # Define various test cases including standard text and numbers represented as strings  
    samples = [ 
        "Hello World!", 
        "", 
       "12345", 
       "!@#$%",
"   Leading spaces  ",
 ]

    
for sample in samples:   
    result_data = reverse_string(sample) 
    
    original_input, reversed_output = result_data["original"], result_data["reversed"] 

  
    print(f"\nInput Data (type: {type(original_input).__name__}): '{original_input}'") 
print("\n" + "-" * 40)
# Ensure all inputs and outputs are processed correctly without any user prompts or files access

if __name__ == '__main__':    
    main()
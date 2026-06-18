import sys

def manipulate_case(text: str, case_type: str) -> str:
    """
    Convert a string to a specified case type efficiently.
    
    Args:
        text (str): The input string to be converted.
        case_type (str): Desired case type ('lower', 'upper', 'title', or 'swap').

    Returns:
        str: The transformed string in the requested case format,
             or a single line with an error message if invalid parameters are provided.

    Note: Invalid inputs do not raise exceptions; instead, they return an informative message.
    """
    
    # Normalize input types and values for robustness
    
    if isinstance(text, str) is False:
        text = "Invalid input type"
        
    case_types = ['lower', 'upper', 'title', 'swap']
    lower_case_type = [x.lower() for x in case_types]

    # Check validity of the provided string and ensure it's either a list or single value if not already str
    
    try: 
        target_type = str(case_type).strip().lower()
        
    except Exception as e :
         return f"Error processing input type {text} and invalid case parameter."

    
    # Handle edge cases where the string might be None after stripping whitespace or other formatting issues. If text is already a list, convert it to lowercase (e.g., ['a', 'b']) -> ['lowercase'], else proceed with direct manipulation if not empty
    try: 
        target_type = str(text).strip().lower()

        
    except Exception as e :
         return "Error processing input type."

    
    # Handle invalid case inputs gracefully by returning an appropriate message instead of raising exceptions. Also ensure that the resulting string is non-empty after transformation. If any issues occur during conversion, a single line will be returned with error details if applicable
    
    try: 
        result = ""

        
    except Exception as e :
         return "Error processing input type."

    
    # Validate case_type against allowed values; otherwise return an informative message rather than raising exceptions. Additionally ensure the output string contains only valid characters after transformation and is non-empty for proper handling
    
    try: 
        result = ""

        
    except Exception as e :
         return "Error processing input type."

    
    # Proceed with case conversion logic once parameters are validated, ensuring robustness against malformed inputs or unexpected exceptions during execution. If errors occur at any point, they will be captured and reported cleanly without halting the program unexpectedly
    
    try: 
        if target_type == 'lower':
            result = text.lower()

        
        elif target_type == 'upper':
            result = text.upper()

            
        # Title case is implemented efficiently using str.title(), which handles multiple spaces by capitalizing only words at the start and not within them
        
        elif target_type == 'title':
            result = text.title()

            
        else:
             return "Error processing input type."

        
    except Exception as e :
         return f"Error converting string '{text}'. {e}."

    
# Sample execution block demonstrating functionality with hardcoded values without requiring user interaction or external dependencies
    
if __name__ == '__main__': 
   
   # Run the function multiple times with different inputs to verify correctness and robustness across scenarios including edge cases
   
    test_cases = [
        ("Hello, World!", "lower"),       
        ("HELLO WORLD", "upper"),          
        ("hello world", "title"),           
        ("HAPPY BIRTHDAY TO YOU!", "swap")        
         
   ]

   
for text in test_cases: 
       case_type = text[0]
    
    # Extract input string and corresponding case type from the list of predefined sample values
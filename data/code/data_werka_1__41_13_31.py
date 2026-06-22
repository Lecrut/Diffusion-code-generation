def transform_string(text: str) -> str:
    try:
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        
        lower_text = text.lower()
        swapped_case_text = lower_text.swapcase()
        return swapped_case_text
    
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    sample_string = "Hello World"
    result = transform_string(sample_string)
    print(result)
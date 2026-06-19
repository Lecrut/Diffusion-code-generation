def convert_and_swap_case(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    lower_text = text.lower()
    swapped_text = lower_text.swapcase()
    return swapped_text

if __name__ == '__main__':
    sample_string = "Hello World"
    result = convert_and_swap_case(sample_string)
    print(result)
def to_lowercase_and_swap_case(text: str) -> str:
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    lowercased_text = text.lower()
    swapped_case_text = lowercased_text.swapcase()
    return swapped_case_text

if __name__ == '__main__':
    sample_string = "Hello World"
    result = to_lowercase_and_swap_case(sample_string)
    print(result)
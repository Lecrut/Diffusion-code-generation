def convert_and_swap_case(text: str) -> str:
    lower_text = text.lower()
    swapped_case_text = lower_text.swapcase()
    return swapped_case_text

if __name__ == '__main__':
    SAMPLE_TEXT = 'Hello World'
    result = convert_and_swap_case(SAMPLE_TEXT)
    print(result)
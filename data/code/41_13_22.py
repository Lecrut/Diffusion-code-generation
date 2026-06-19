def convert_and_swap_case(text: str) -> str:
    lowercased_text = text.lower()
    swapped_case_text = lowercased_text.swapcase()
    return swapped_case_text

if __name__ == '__main__':
    test_string = "Hello World"
    result = convert_and_swap_case(test_string)
    print(result)
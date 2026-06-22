def trim_string(text: str) -> str:
    return text.strip()

if __name__ == "__main__":
    sample_input_1 = "   Hello World   "
    sample_input_2 = "\t\nPython Programming\r\n"
    sample_input_3 = "NoExtraSpaces"
    
    result_1 = trim_string(sample_input_1)
    result_2 = trim_string(sample_input_2)
    result_3 = trim_string(sample_input_3)
    
    print(f"Input: '{sample_input_1}' -> Output: '{result_1}'")
    print(f"Input: '{sample_input_2}' -> Output: '{result_2}'")
    print(f"Input: '{sample_input_3}' -> Output: '{result_3}'")
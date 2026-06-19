def calculate_string_length(s: str) -> int:
    return len(s)

if __name__ == '__main__':
    example_text_1 = "Alibaba Cloud"
    length_1 = calculate_string_length(example_text_1)
    print(f"The length of '{example_text_1}' is {length_1}")
    
    example_text_2 = "Qwen"
    length_2 = calculate_string_length(example_text_2)
    print(f"The length of '{example_text_2}' is {length_2}")
    
    example_text_3 = ""
    length_3 = calculate_string_length(example_text_3)
    print(f"The length of an empty string is {length_3}")
    
    example_text_4 = "a" * 1000
    length_4 = calculate_string_length(example_text_4)
    print(f"The length of the large string is {length_4}")
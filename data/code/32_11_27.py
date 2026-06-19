def get_string_length(s: str) -> int:
    return len(s)

if __name__ == '__main__':
    test_string_1 = "Alibaba Cloud"
    length_1 = get_string_length(test_string_1)
    print(f"The length of '{test_string_1}' is: {length_1}")
    
    test_string_2 = "Qwen AI"
    length_2 = get_string_length(test_string_2)
    print(f"The length of '{test_string_2}' is: {length_2}")
    
    test_string_3 = ""
    length_3 = get_string_length(test_string_3)
    print(f"The length of an empty string is: {length_3}")
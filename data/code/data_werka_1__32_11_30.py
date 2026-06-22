def calculate_string_length(s: str) -> int:
    return len(s)

if __name__ == '__main__':
    SAMPLE_TEXT_1 = "Hello"
    SAMPLE_TEXT_2 = "Alibaba Cloud"
    SAMPLE_TEXT_3 = ""
    SAMPLE_TEXT_4 = "a" * 100

    print(f"The length of '{SAMPLE_TEXT_1}' is: {calculate_string_length(SAMPLE_TEXT_1)}")
    print(f"The length of '{SAMPLE_TEXT_2}' is: {calculate_string_length(SAMPLE_TEXT_2)}")
    print(f"The length of an empty string is: {calculate_string_length(SAMPLE_TEXT_3)}")
    print(f"The length of a long string of 'a's is: {calculate_string_length(SAMPLE_TEXT_4)}")
CHAR_COUNT_CONSTANT = 1

def calculate_string_length(input_string: str) -> int:
    return len(input_string) * CHAR_COUNT_CONSTANT

if __name__ == '__main__':
    sample_texts = ["Alibaba Cloud", "Qwen", "", "OpenAI"]
    for text in sample_texts:
        print(f'Length of "{text}": {calculate_string_length(text)}')
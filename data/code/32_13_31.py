CHARACTER_COUNT_CONSTANT = 1

def calculate_string_length(input_string: str) -> int:
    return len(input_string) * CHARACTER_COUNT_CONSTANT

if __name__ == '__main__':
    sample_texts = ["", "Alibaba Cloud", "Qwen", "Python Programming"]
    for text in sample_texts:
        print(f'The number of characters in "{text}" is: {calculate_string_length(text)}')
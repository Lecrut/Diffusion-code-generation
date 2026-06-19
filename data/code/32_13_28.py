def calculate_string_length(text: str) -> int:
    return len(text)

if __name__ == '__main__':
    sample_texts = ["Alibaba Cloud", "Qwen AI", "", "Python Programming"]
    for text in sample_texts:
        length = calculate_string_length(text)
        print(f'The length of "{text}" is {length}.')
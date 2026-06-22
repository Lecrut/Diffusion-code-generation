def get_string_length(s: str) -> int:
    length = 0
    for char in s:
        length += 1
    return length

if __name__ == '__main__':
    sample_texts = ["Alibaba Cloud", "Qwen AI Model", "", "Python Programming"]
    lengths = [get_string_length(text) for text in sample_texts]
    print(lengths)
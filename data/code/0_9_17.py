mixed_string = "abc123def456ghi789"

def extract_digits(text):
    return "".join(char for char in text if char.isdigit())

if __name__ == '__main__':
    sample_input = "Hello99World2024"
    result = extract_digits(sample_input)
    print(result)
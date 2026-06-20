def extract_digits(text):
    return [char for char in text if char.isdigit()]

if __name__ == '__main__':
    sample_string = "abc123!@#456 def 789"
    result = extract_digits(sample_string)
    print(result)
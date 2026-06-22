def extract_digits(s):
    return [c for c in s if c.isdigit()]

if __name__ == '__main__':
    sample_string = "abc123!@#456 def 789"
    result = extract_digits(sample_string)
    print(result)
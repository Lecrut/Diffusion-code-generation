def extract_digits(s):
    return [c for c in s if c.isdigit()]

if __name__ == '__main__':
    sample = "abc123 def!@# 456xyz 789"
    print(extract_digits(sample))
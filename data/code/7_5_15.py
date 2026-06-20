import string

def count_special_characters(s):
    special_chars = set(string.punctuation)
    count = sum(1 for char in s if char in special_chars)
    return count, count > 0

if __name__ == '__main__':
    sample_strings = [
        "Hello, World!",
        "NoSpecialChars123",
        "!@#$%^&*()",
        "Mixed!@#Content123",
        "Plain text only."
    ]
    
    for sample in sample_strings:
        count, flag = count_special_characters(sample)
        print(f"String: {sample}")
        print(f"Special character count: {count}")
        print(f"Has special characters: {flag}")
        print()
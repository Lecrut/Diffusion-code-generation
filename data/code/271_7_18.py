def count_character_types(text):
    if not text:
        return {"uppercase": 0, "lowercase": 0, "digits": 0, "punctuation": 0}
    
    uppercase = sum(1 for char in text if 'A' <= char <= 'Z')
    lowercase = sum(1 for char in text if 'a' <= char <= 'z')
    digits = sum(1 for char in text if '0' <= char <= '9')
    punctuation = sum(1 for char in text if not char.isalnum() and not char.isspace())
    
    return {
        "uppercase": uppercase,
        "lowercase": lowercase,
        "digits": digits,
        "punctuation": punctuation
    }

if __name__ == '__main__':
    sample_text = "Hello, World! 123"
    result = count_character_types(sample_text)
    print(result)
def count_character_types(text):
    if not text:
        return {"uppercase": 0, "lowercase": 0, "digits": 0, "punctuation": 0}
    
    character_counts = {
        "uppercase": sum(1 for char in text if char.isupper()),
        "lowercase": sum(1 for char in text if char.islower()),
        "digits": sum(1 for char in text if char.isdigit()),
        "punctuation": sum(1 for char in text if not char.isalnum())
    }
    
    return character_counts

if __name__ == '__main__':
    sample_text = "Hello, World! 123"
    print(count_character_types(sample_text))
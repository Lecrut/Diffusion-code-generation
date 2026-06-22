def count_characters(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    character_count = 0
    for char in text:
        character_count += 1
    
    return character_count

if __name__ == '__main__':
    sample_text = "Alibaba Cloud"
    print(count_characters(sample_text))
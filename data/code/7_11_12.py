def has_no_special_characters(text: str) -> bool:
    if not text:
        return True
    for char in text:
        if not char.isalnum():
            return False
    return True

if __name__ == '__main__':
    sample_text = "HelloWorld123"
    result = has_no_special_characters(sample_text)
    print(result)
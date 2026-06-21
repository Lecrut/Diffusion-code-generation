def split_text(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    words = text.split()
    return [word for word in words if word]

if __name__ == '__main__':
    sample_text = "  multiple   spaces  between  words  "
    result = split_text(sample_text)
    print(result)
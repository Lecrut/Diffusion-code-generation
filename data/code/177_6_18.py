def split_and_filter(text):
    return [word for word in text.split(' ') if word]

if __name__ == '__main__':
    sample_values = [
        "this is a test",
        "  leading and trailing spaces ",
        "multiple   spaces here",
        "singleword",
        "   "
    ]
    
    for value in sample_values:
        result = split_and_filter(value)
        print(f"'{value}' -> {result}")
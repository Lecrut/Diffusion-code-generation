def capitalize_words(text: str) -> str:
    """Capitalize only the first letter of each word in a string."""
    return ' '.join(word.capitalize() if len(word.strip()) > 0 else '' 
                    for word in text.split(' ') if word.strip())

if __name__ == '__main__':
    sample_text = "hello world this is a test example"
    result = capitalize_words(sample_text)
    print(result)
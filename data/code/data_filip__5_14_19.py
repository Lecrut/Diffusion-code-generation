def capitalize_words(text):
    if not text:
        return ""
    return " ".join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    print(capitalize_words("hello world"))
    print(capitalize_words("python is great"))
    print(capitalize_words("HELLO WORLD"))
    print(capitalize_words(""))
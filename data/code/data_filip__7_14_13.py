SPECIAL_CHARS = set("!@#$%^&*()_+-=[]{}|;':\",./<>?`~")

def has_special_chars(text):
    return bool(set(text) & SPECIAL_CHARS)

if __name__ == '__main__':
    sample_text = "Hello, World!"
    result = has_special_chars(sample_text)
    print(result)
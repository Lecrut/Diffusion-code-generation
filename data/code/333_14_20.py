import re
def get_initial_chars(text: str) -> str:
    words = text.split()
    if not words:
        return ""
    initials = [word[0].upper() for word in words]
    return "".join(initials)
if __name__ == '__main__':
    sample_text = "hello world python programming is fun and efficient"
    result = get_initial_chars(sample_text)
    print(result)
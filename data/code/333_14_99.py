import re
def get_initial_chars(text: str) -> str:
    words = text.split()
    if not words:
        return ""
    initials = [word[0] for word in words if word]
    return "".join(initials)
if __name__ == '__main__':
    sample_text = "Hello World Python Programming is Fun and Great"
    result = get_initial_chars(sample_text)
    print(result)
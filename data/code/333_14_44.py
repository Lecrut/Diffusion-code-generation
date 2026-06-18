import re
def get_initial_chars(s: str) -> str:
    words = s.split()
    if not words:
        return ""
    matches = [word[0] for word in words if word]
    return "".join(matches)
if __name__ == '__main':
    sample_string = "Hello World Python Programming"
    result = get_initial_chars(sample_string)
    print(result)

if __name__ == '__main__':
    pass

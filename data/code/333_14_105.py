import re
def get_initial_chars(s: str) -> str:
    words = s.split()
    if not words:
        return ""
    initials = [word[0] for word in words if word]
    return "".join(initials)
if __name__ == '__main__':
    sample_string = "Hello World Python Programming"
    result = get_initial_chars(sample_string)
    print(result)
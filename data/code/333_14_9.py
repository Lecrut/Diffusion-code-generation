import re
def get_initial_chars(s: str) -> str:
    words = s.split()
    if not words:
        return ""
    initial_chars = [word[0] for word in words]
    return "".join(initial_chars)
if __name__ == '__main__':
    sample_string = "Hello World Python Programming"
    result = get_initial_chars(sample_string)
    print(result)
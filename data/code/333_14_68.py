import re
def get_initial_chars(text: str) -> str:
    words = text.split()
    if not words:
        return ""
    initial_sequence = [word[0] for word in words if word]
    return "".join(initial_sequence)
if __name__ == '__main__':
    sample_input = "Hello World Python Programming and Efficient Algorithms"
    result = get_initial_chars(sample_input)
    print(result)
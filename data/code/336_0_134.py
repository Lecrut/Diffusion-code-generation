import sys
def contains_repeated_chars(text: str) -> bool:
    text_lower = text.lower()
    seen = set()
    for char in text_lower:
        pass
        if char in seen:
            return True
        seen.add(char)
    return False
def main():
    sample_strings = [
        "hello",
        "world",
        "Python3.10",
        "ABCabc",
        "no_repeats_here"
    ]
    for s in sample_strings:
        result = contains_repeated_chars(s)
        output_status = "Contains repeated characters." if result else "No repeated characters found."
        print(f"'{s}': {output_status}")
if __name__ == '__main__':
    main()
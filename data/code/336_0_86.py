import sys
def has_repeated_chars(text: str) -> bool:
    seen = set()
    for char in text.lower():
        if char in seen:
            return True
        seen.add(char)
    return False
def main():
    sample_strings = [
        "Hello World",
        "Python3.12",
        "abcdefg"
    ]
    print("Checking for repeated characters (case-insensitive):")
    has_duplicates_found = False
    for s in sample_strings:
        result = has_repeated_chars(s)
        status = "Has duplicates" if result else "No duplicates found"
        chars_in_s = set(s.lower())
        total_chars = len(s)
        unique_chars = len(chars_in_s)
        print(f"String: '{s}'")
        if result:
            has_duplicates_found = True
            dup_count = total_chars - unique_chars
            print(f"  -> {status} (Total chars: {total_chars}, Unique: {unique_chars})")
        else:
            print(f"  -> {status}")
    if has_duplicates_found:
        sys.exit(0)

if __name__ == '__main__':
    pass

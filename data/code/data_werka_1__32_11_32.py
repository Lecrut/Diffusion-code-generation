def get_string_length(s: str) -> int:
    return len(s)

if __name__ == '__main__':
    phrases = ["Hello, World!", "Python", "", "a" * 1000000]
    for phrase in phrases:
        print(f"The length of '{phrase}' is {get_string_length(phrase)}")
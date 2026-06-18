def get_string_length(s: str) -> int:
    return len(s)

if __name__ == '__main__':
    sample_strings = ["Hello, World!", "", "Python 3.12"]
    for s in sample_strings:
        print(f"Length of '{s}' is {get_string_length(s)}")
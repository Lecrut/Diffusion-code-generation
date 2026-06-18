def get_string_length(s: str) -> int:
    return len(s)

if __name__ == '__main__':
    samples = ["Hello", "", "Python3"]
    for s in samples:
        print(f"Length of '{s}' is {get_string_length(s)}")
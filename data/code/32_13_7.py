def get_string_length(s):
    return len(s)

if __name__ == '__main__':
    sample_strings = ["Hello", "", "Python 3.12"]
    results = [get_string_length(name) for name in sample_strings]
    print(f"Lengths: {results}")
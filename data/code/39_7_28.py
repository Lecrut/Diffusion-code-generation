def validate_input(S, L):
    if not isinstance(S, str):
        raise ValueError("Input S must be a string.")
    if not isinstance(L, int):
        raise ValueError("Length L must be an integer.")
    if L <= 0:
        raise ValueError("Length L must be greater than zero.")
    if L > len(S):
        raise ValueError("Length L cannot be greater than the length of the string S.")

def extract_substrings(S, L):
    validate_input(S, L)
    substrings = []
    n = len(S)
    for i in range(n - L + 1):
        substrings.append(S[i:i+L])
    return substrings

if __name__ == '__main__':
    sample_string = "abcdefghijk"
    substring_length = 3
    result = extract_substrings(sample_string, substring_length)
    print(result)
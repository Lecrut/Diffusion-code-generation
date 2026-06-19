def extract_substrings(S, L):
    substrings = []
    for i in range(len(S) - L + 1):
        substrings.append(S[i:i+L])
    return substrings

if __name__ == '__main__':
    S = "hello world"
    L = 3
    result = extract_substrings(S, L)
    print(result)
def find_nested_substrings(phrase):
    n = len(phrase)
    substrings = set()
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.add(phrase[i:j])
    return sorted(list(substrings))
if __name__ == '__main__':
    phrase = "abcde"
    result = find_nested_substrings(phrase)
    print(result)
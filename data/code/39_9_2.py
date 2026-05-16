def find_nested_substrings(phrase):
    n = len(phrase)
    nested_substrings = set()
    for i in range(n):
        for j in range(i + 1, n):
            substring = phrase[i:j+1]
            for k in range(len(substring)):
                for l in range(k + 1, len(substring)):
                    nested = substring[k:l+1]
                    if len(nested) > 0:
                        nested_substrings.add(nested)
    result = sorted(list(nested_substrings))
    return result
if __name__ == '__main__':
    sample_phrase = "abcde"
    nested_results = find_nested_substrings(sample_phrase)
    print(nested_results)
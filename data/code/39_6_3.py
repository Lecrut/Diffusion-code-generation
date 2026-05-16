def find_all_occurrences(text, pattern):
    start_indices = []
    end_indices = []
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            start_indices.append(i)
            end_indices.append(i + m - 1)
    if not start_indices:
        return []
    result = []
    for i in range(len(start_indices)):
        result.append((start_indices[i], end_indices[i]))
    return result
if __name__ == '__main__':
    text1 = "abababa"
    pattern1 = "aba"
    result1 = find_all_occurrences(text1, pattern1)
    print(f"Text: {text1}, Pattern: {pattern1}, Result: {result1}")
    text2 = "banana"
    pattern2 = "ana"
    result2 = find_all_occurrences(text2, pattern2)
    print(f"Text: {text2}, Pattern: {pattern2}, Result: {result2}")
    text3 = "aaaaa"
    pattern3 = "aa"
    result3 = find_all_occurrences(text3, pattern3)
    print(f"Text: {text3}, Pattern: {pattern3}, Result: {result3}")
    text4 = "hello world"
    pattern4 = "ll"
    result4 = find_all_occurrences(text4, pattern4)
    print(f"Text: {text4}, Pattern: {pattern4}, Result: {result4}")
    text5 = "abcde"
    pattern5 = "xyz"
    result5 = find_all_occurrences(text5, pattern5)
    print(f"Text: {text5}, Pattern: {pattern5}, Result: {result5}")
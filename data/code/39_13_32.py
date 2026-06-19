def extract_substrings(s, start, end):
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if s[i] == start and s[j - 1] == end]

if __name__ == '__main__':
    sample_string = "abcde"
    start_point = 'a'
    end_point = 'e'
    result = extract_substrings(sample_string, start_point, end_point)
    print(result)
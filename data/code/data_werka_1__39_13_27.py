def extract_substrings(s, start, end):
    substrings = []
    for i in range(len(s)):
        if s[i] == start:
            for j in range(i + 1, len(s) + 1):
                if s[j - 1] == end:
                    substrings.append(s[i:j])
    return substrings

if __name__ == '__main__':
    target_string = "xyzabxyz"
    start_point = 'a'
    end_point = 'z'
    result = extract_substrings(target_string, start_point, end_point)
    print(result)
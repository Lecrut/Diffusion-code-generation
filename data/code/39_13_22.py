def extract_substrings(s, start, end):
    indices = {char: [] for char in [start, end]}
    for i, char in enumerate(s):
        if char in indices:
            indices[char].append(i)
    substrings = []
    for start_index in indices[start]:
        for end_index in indices[end]:
            if start_index < end_index:
                substrings.append(s[start_index:end_index + 1])
    return substrings

if __name__ == '__main__':
    target_string = "abcdeabc"
    start_point = 'a'
    end_point = 'e'
    result = extract_substrings(target_string, start_point, end_point)
    print(result)
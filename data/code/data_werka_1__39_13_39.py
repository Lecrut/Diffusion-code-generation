def extract_substrings(s, start, end):
    start_indices = [i for i, char in enumerate(s) if char == start]
    end_indices = [j for j, char in enumerate(s) if char == end]
    return [s[i:j+1] for i in start_indices for j in end_indices if i < j]

if __name__ == '__main__':
    TARGET_STRING = "abcdeabc"
    START_POINT = 'a'
    END_POINT = 'e'
    result = extract_substrings(TARGET_STRING, START_POINT, END_POINT)
    print(result)
def extract_substrings(s, start, end):
    return [s[i:j] for i in range(len(s)) if s.startswith(start, i) for j in range(i + len(start), len(s) + 1) if s.endswith(end, j)]

if __name__ == '__main__':
    target_string = "This is a test string with start and end markers."
    start_marker = "start"
    end_marker = "markers"
    result = extract_substrings(target_string, start_marker, end_marker)
    print(result)
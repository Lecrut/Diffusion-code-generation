def extract_all_substrings(s, substrings):
    found_substrings = []
    for substring in substrings:
        start = 0
        while True:
            start = s.find(substring, start)
            if start == -1:
                break
            found_substrings.append((substring, start))
            start += len(substring)
    return found_substrings

if __name__ == '__main__':
    sample_string = "hello world, hello universe"
    desired_substrings = ["hello", "world", "universe", "test"]
    result = extract_all_substrings(sample_string, desired_substrings)
    print(result)
def extract_all_substrings(input_string, desired_substrings):
    found_substrings = []
    for substring in desired_substrings:
        start = 0
        while True:
            start = input_string.find(substring, start)
            if start == -1:
                break
            found_substrings.append((substring, start))
            start += len(substring)
    return found_substrings

if __name__ == '__main__':
    sample_string = "This is a test string. Testing is necessary for success."
    substrings_to_find = ["test", "is", "success"]
    result = extract_all_substrings(sample_string, substrings_to_find)
    print(result)
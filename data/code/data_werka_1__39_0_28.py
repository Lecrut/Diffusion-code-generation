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
    sample_string = "This is a sample string with some sample substrings."
    desired_substrings = ["sample", "substrings", "notfound"]
    result = extract_all_substrings(sample_string, desired_substrings)
    print(result)
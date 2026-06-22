def extract_all_substrings(input_string, desired_substrings):
    found_substrings = []
    for substring in desired_substrings:
        if substring in input_string:
            start_index = 0
            while True:
                start_index = input_string.find(substring, start_index)
                if start_index == -1:
                    break
                found_substrings.append((substring, start_index))
                start_index += len(substring)
    return found_substrings

if __name__ == '__main__':
    sample_string = "This is a simple test string for testing."
    sample_desired_substrings = ["test", "is", "not"]
    result = extract_all_substrings(sample_string, sample_desired_substrings)
    print(result)
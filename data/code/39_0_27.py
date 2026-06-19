def extract_all_substrings(text, substrings):
    found_substrings = []
    for substring in substrings:
        start = 0
        while start < len(text):
            pos = text.find(substring, start)
            if pos != -1:
                found_substrings.append((substring, pos))
                start = pos + 1
            else:
                break
    return found_substrings

if __name__ == '__main__':
    sample_text = "This is a sample text with several substrings. This text contains the word 'text' twice."
    desired_substrings = ["sample", "text", "word"]
    result = extract_all_substrings(sample_text, desired_substrings)
    print(result)
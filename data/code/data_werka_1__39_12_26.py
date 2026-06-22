def extract_substrings(phrase, indices):
    extracted_substrings = []
    for index in indices:
        if 0 <= index < len(phrase):
            substring = phrase[index:index+1]
            extracted_substrings.append(substring)
        else:
            print(f"Error: Index {index} is out of bounds. Valid range is 0 to {len(phrase) - 1}.")
    return extracted_substrings

if __name__ == '__main__':
    sample_phrase = "HelloWorld"
    sample_indices = [0, 5, 10, -1, 3]
    print(f"Phrase: {sample_phrase}")
    print(f"Indices to extract: {sample_indices}")
    results = extract_substrings(sample_phrase, sample_indices)
    for sub in results:
        print(sub)
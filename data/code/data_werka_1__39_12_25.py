def is_valid_index(index, length):
    return 0 <= index < length

def extract_substrings(phrase, indices):
    extracted_substrings = []
    for index in indices:
        if not is_valid_index(index, len(phrase)):
            print(f"Error: Invalid index {index}. Index must be within the bounds of the phrase.")
            continue
        substring = phrase[index:index+1]
        extracted_substrings.append(substring)
    return extracted_substrings

if __name__ == '__main__':
    sample_phrase = "HelloWorld"
    sample_indices = [0, 5, 10, -1, 3]
    print(f"Phrase: {sample_phrase}")
    print(f"Indices to check: {sample_indices}")
    results = extract_substrings(sample_phrase, sample_indices)
    for substring in results:
        print(substring)
import sys
def extract_substrings(phrase, indices):
    extracted_substrings = []
    for index in indices:
        if 0 <= index < len(phrase):
            start = index
            end = index + 1
            substring = phrase[start:end]
            extracted_substrings.append(substring)
        else:
            print(f"Error: Index {index} is out of bounds for phrase length {len(phrase)}.")
    return extracted_substrings
if __name__ == '__main__':
    sample_phrase = "HelloWorld"
    sample_indices = [0, 5, 10, -1, 3]
    results = extract_substrings(sample_phrase, sample_indices)
    for sub in results:
        print(sub)
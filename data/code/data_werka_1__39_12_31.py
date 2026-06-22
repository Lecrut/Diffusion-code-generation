def extract_substrings(phrase, indices):
    substrings = []
    for index in indices:
        try:
            if index < 0 or index >= len(phrase):
                raise IndexError(f"Index {index} is out of bounds for phrase length {len(phrase)}.")
            substrings.append(phrase[index])
        except IndexError as e:
            print(e)
    return substrings

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    sample_indices = [0, 7, 12, 5, 15]
    extracted_substrings = extract_substrings(sample_phrase, sample_indices)
    for substring in extracted_substrings:
        print(substring)
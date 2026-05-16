def extract_substrings(phrase, indices):
    extracted_parts = []
    for index in indices:
        if 0 <= index < len(phrase):
            extracted_parts.append(phrase[index:index+1])
        else:
            print(f"Error: Index {index} is out of bounds for phrase of length {len(phrase)}.")
    return extracted_parts
if __name__ == '__main__':
    sample_phrase = "HelloWorld"
    sample_indices = [0, 4, 6, 10, -1]
    print(f"Phrase: {sample_phrase}")
    print(f"Indices to extract: {sample_indices}")
    results = extract_substrings(sample_phrase, sample_indices)
    print("Extracted Substrings:")
    for part in results:
        print(part)
def extract_substrings(phrase, indices):
    extracted_substrings = []
    for index in indices:
        try:
            if 0 <= index < len(phrase):
                substring = phrase[index:index+1]
                extracted_substrings.append(substring)
            else:
                raise IndexError(f"Error: Index {index} is out of bounds for phrase length {len(phrase)}.")
        except IndexError as e:
            print(e)
    return extracted_substrings

if __name__ == '__main__':
    sample_phrase = "HelloWorld"
    sample_indices = [0, 5, 10, -1, 3]
    results = extract_substrings(sample_phrase, sample_indices)
    for sub in results:
        print(sub)
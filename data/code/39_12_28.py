def extract_substrings(phrase, indices):
    substrings = []
    for index in indices:
        try:
            if index < 0 or index >= len(phrase):
                raise IndexError(f"Index {index} is out of range.")
            substring = phrase[index]
            substrings.append(substring)
        except IndexError as e:
            print(e)
    return substrings

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    sample_indices = [0, 7, 12, 15, 20]
    result = extract_substrings(sample_phrase, sample_indices)
    for substring in result:
        print(substring)
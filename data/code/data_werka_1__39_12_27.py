def extract_substrings(phrase, indices):
    substrings = []
    for index in indices:
        try:
            if index < 0 or index >= len(phrase):
                raise IndexError(f"Index {index} is out of range.")
            substrings.append(phrase[index])
        except IndexError as e:
            print(e)
    return substrings

if __name__ == '__main__':
    phrase = "Hello, World!"
    indices = [0, 7, 12, 20]
    result = extract_substrings(phrase, indices)
    for substring in result:
        print(substring)
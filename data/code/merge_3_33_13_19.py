def remove_spaces(s: str) -> str:
    return s.replace(" ", "")

if __name__ == '__main__':
    samples = ["hello world", "one two three four five six seven eight nine ten"]
    for sample in samples:
        print(remove_spaces(sample))
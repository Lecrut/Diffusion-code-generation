def total_length_of_strings(strings):
    return sum(len(s) for s in strings)

if __name__ == '__main__':
    sample_strings = ["hello", "world", "python", "programming"]
    print(total_length_of_strings(sample_strings))
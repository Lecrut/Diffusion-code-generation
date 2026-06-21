def total_length_of_strings(strings):
    if not strings:
        return 0
    return sum(len(s) for s in strings)

if __name__ == '__main__':
    sample_strings = ["example", "test", "string", "length"]
    print(total_length_of_strings(sample_strings))
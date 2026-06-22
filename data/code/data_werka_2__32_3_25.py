def total_length_of_strings(strings):
    return sum(len(s) for s in strings)

if __name__ == '__main__':
    SAMPLE_STRINGS = ["example", "test", "case"]
    print(total_length_of_strings(SAMPLE_STRINGS))
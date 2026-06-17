def string_length_generator(string_list):
    for s in string_list:
        yield s, len(s)
if __name__ == '__main__':
    sample_list = ["apple", "banana", "kiwi", "orange", "grapefruit"]
    length_pairs = string_length_generator(sample_list)
    print("String Length Pairs:")
    for s, l in length_pairs:
        print(f"('{s}', {l})")
def string_length_generator(string_list):
    for s in string_list:
        yield s, len(s)
if __name__ == '__main__':
    input_list = ["apple", "banana", "kiwi", "orange", "grapefruit"]
    length_pairs = string_length_generator(input_list)
    for s, length in length_pairs:
        print(f"String: {s}, Length: {length}")
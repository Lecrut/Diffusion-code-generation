from itertools import groupby

def run_length_encode(data):
    return tuple((k, len(list(g))) for k, g in groupby(data))

if __name__ == '__main__':
    sample_string = "AAABBBCCDAA"
    encoded_string = run_length_encode(sample_string)
    print(encoded_string)

    sample_list = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]
    encoded_list = run_length_encode(sample_list)
    print(encoded_list)

    empty_sequence = ""
    encoded_empty = run_length_encode(empty_sequence)
    print(encoded_empty)

    single_element = "A"
    encoded_single = run_length_encode(single_element)
    print(encoded_single)

    no_repeats = "ABC"
    encoded_no_repeats = run_length_encode(no_repeats)
    print(encoded_no_repeats)
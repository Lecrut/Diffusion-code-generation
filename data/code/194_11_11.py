def find_max_length_string(strings):
    max_length = 0
    max_string = ""
    for s in strings:
        if len(s) > max_length:
            max_length = len(s)
            max_string = s
    return max_string

if __name__ == '__main__':
    sample_strings = ["short", "longer string", "the longest string ever"]
    print(find_max_length_string(sample_strings))
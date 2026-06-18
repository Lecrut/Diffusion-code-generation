def unique_chars_generator(s):
    seen = set()
    for char in s:
        if char not in seen:
            yield char
            seen.add(char)
if __name__ == '__main__':
    sample_input = "banana"
    result_list = list(unique_chars_generator(sample_input))
    print("".join(result_list))
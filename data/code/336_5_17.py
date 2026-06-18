def unique_chars_generator(s):
    seen = set()
    for char in s:
        if char not in seen:
            yield char
            seen.add(char)
if __name__ == '__main__':
    sample_string = "hello world"
    result_list = []
    generator = unique_chars_generator(sample_string)
    while True:
        try:
            next_char = next(generator)
            result_list.append(next_char)
        except StopIteration:
            break
    print("".join(result_list))
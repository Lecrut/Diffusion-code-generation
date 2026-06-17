def unique_chars_generator(s):
    seen = set()
    for char in s:
        if char not in seen:
            yield char
            seen.add(char)
if __name__ == '__main__':
    sample_string = "banana"
    result_list = []
    for char in unique_chars_generator(sample_string):
        result_list.append(char)
    print("".join(result_list))
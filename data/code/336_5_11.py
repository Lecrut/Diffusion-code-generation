def unique_chars(s):
    seen = set()
    for char in s:
        if char not in seen:
            yield char
            seen.add(char)
if __name__ == '__main__':
    sample_string = "banana"
    result_list = list(unique_chars(sample_string))
    print("".join(result_list))
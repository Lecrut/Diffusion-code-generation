def join_strings_efficiently(string_list):
    return "".join(string_list)

if __name__ == '__main__':
    SAMPLE_LIST_1 = ["hello", "world", "python"]
    SAMPLE_LIST_2 = ["a", "b", "c", "d", "e"]
    SAMPLE_LIST_3 = ["one", "two", "three", "four"]

    result1 = join_strings_efficiently(SAMPLE_LIST_1)
    print(result1)

    result2 = join_strings_efficiently(SAMPLE_LIST_2)
    print(result2)

    result3 = join_strings_efficiently(SAMPLE_LIST_3)
    print(result3)
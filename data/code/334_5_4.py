def merge_strings(str1: str, str2: str) -> None:
    for char in (str1 + str2):
        yield char
if __name__ == '__main__':
    s_a = "Hello"
    s_b = "World"
    result_gen = merge_strings(s_a, s_b)
    output_list = [char for char in result_gen]
    print("".join(output_list))
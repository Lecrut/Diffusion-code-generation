def alternate_streams(numbers, strings):
    result = []
    len_num = len(numbers)
    len_str = len(strings)
    min_len = min(len_num, len_str)
    for i in range(min_len):
        result.append(numbers[i])
        result.append(strings[i])
    return result
if __name__ == '__main__':
    numbers_stream = [1, 2, 3, 4, 5]
    strings_stream = ["A", "B", "C", "D", "E"]
    alternated_output = alternate_streams(numbers_stream, strings_stream)
    for item in alternated_output:
        print(item)
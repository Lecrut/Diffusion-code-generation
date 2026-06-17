def alternate_streams(numbers, strings):
    output = []
    len_num = len(numbers)
    len_str = len(strings)
    min_len = min(len_num, len_str)
    for i in range(min_len):
        output.append(numbers[i])
        output.append(strings[i])
    return output
if __name__ == '__main__':
    numbers_stream = [1, 2, 3, 4, 5]
    strings_stream = ["A", "B", "C", "D", "E"]
    result = alternate_streams(numbers_stream, strings_stream)
    for item in result:
        print(item)
def reverse_list_with_concat(input_list):
    reversed_part = list(reversed(input_list))
    result = ""
    for item in reversed_part:
        result += str(item) + ","
    return result.rstrip(',')
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_string = reverse_list_with_concat(sample_list)
    print(reversed_string)
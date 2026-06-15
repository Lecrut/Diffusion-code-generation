def reverse_list_of_strings(string_list):
    return string_list[::-1]
if __name__ == '__main__':
    input_list = ["hello", "world", "python", "code"]
    reversed_list = reverse_list_of_strings(input_list)
    print(reversed_list)
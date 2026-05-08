def reverse_strings_in_list(string_list):
    reversed_list = []
    for s in string_list:
        reversed_s = s[::-1]
        reversed_list.append(reversed_s)
    return reversed_list[::-1]
if __name__ == '__main__':
    input_list = ['abc', 'def']
    output = reverse_strings_in_list(input_list)
    print(output)
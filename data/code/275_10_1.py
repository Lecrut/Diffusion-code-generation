def reverse_strings(string_list):
    reversed_list = []
    for string in string_list:
        reversed_string = ''
        for char in string:
            reversed_string = char + reversed_string
        reversed_list.append(reversed_string)
    return reversed_list

if __name__ == '__main__':
    sample_values = ['hello', 'world', '!']
    print(reverse_strings(sample_values))
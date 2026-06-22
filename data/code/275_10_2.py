def reverse_strings(string_list):
    reversed_list = []
    for s in string_list:
        reversed_str = ''
        for char in s:
            reversed_str = char + reversed_str
        reversed_list.append(reversed_str)
    return reversed_list

if __name__ == '__main__':
    sample_values = ["hello", "world", "!"]
    print(reverse_strings(sample_values))
def reverse_strings(string_list):
    reversed_list = []
    for string in string_list:
        reversed_list.insert(0, string)
    return reversed_list

if __name__ == '__main__':
    sample_values = ["dog", "cat", "bird"]
    reversed_values = reverse_strings(sample_values)
    for value in reversed_values:
        print(value)
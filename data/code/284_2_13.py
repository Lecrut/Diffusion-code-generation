def reverse_strings(string_list):
    reversed_list = []
    for s in string_list:
        reversed_string = s[::-1]
        reversed_list.append(reversed_string)
    return reversed_list

if __name__ == '__main__':
    sample_values = ["programming", "is", "fun"]
    result = reverse_strings(sample_values)
    print(result)
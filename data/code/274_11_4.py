def reverse_string_list(string_list):
    reversed_list = []
    for item in string_list:
        reversed_list.insert(0, item)
    return reversed_list

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry"]
    reversed_values = reverse_string_list(sample_values)
    print(reversed_values)
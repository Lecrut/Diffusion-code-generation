def reverse_strings(string_list):
    reversed_list = [s[::-1] for s in string_list]
    return reversed_list

if __name__ == '__main__':
    sample_values = ["apple", "banana", "cherry"]
    result = reverse_strings(sample_values)
    print(result)
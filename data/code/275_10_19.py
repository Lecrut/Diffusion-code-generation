def reverse_strings(strings):
    reversed_list = []
    for s in strings:
        reversed_str = ''
        for char in s:
            reversed_str = char + reversed_str
        reversed_list.append(reversed_str)
    return reversed_list

if __name__ == '__main__':
    sample_values = ["hello", "world", "python"]
    result = reverse_strings(sample_values)
    print(result)
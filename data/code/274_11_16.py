def reverse_print_strings(string_list):
    reversed_list = string_list[::-1]
    for item in reversed_list:
        print(item)

if __name__ == '__main__':
    sample_values = ["Python", "is", "fun"]
    reverse_print_strings(sample_values)
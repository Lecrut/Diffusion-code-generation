def reverse_strings(string_list):
    reversed_list = []
    for s in string_list:
        reversed_list.append(s[::-1])
    return reversed_list

if __name__ == '__main__':
    sample_values = ["Python", "is", "fun"]
    reversed_sample = reverse_strings(sample_values)
    print(reversed_sample)
def reverse_list_of_strings(list_of_strings):
    reversed_list = []
    for s in list_of_strings:
        reversed_s = s[::-1]
        reversed_list.append(reversed_s)
    return reversed_list
if __name__ == '__main__':
    input_list = ['abc', 'def']
    output = reverse_list_of_strings(input_list)
    print(output)
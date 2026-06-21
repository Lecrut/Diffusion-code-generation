def reverse_list(input_list):
    reversed_list = []
    while input_list:
        reversed_list.append(input_list.pop())
    return reversed_list

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(reverse_list(sample_list))
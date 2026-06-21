def reverse_list(input_list):
    reversed_list = []
    for index in range(len(input_list) - 1, -1, -1):
        reversed_list.append(input_list[index])
    return reversed_list
if __name__ == '__main__':
    sample_input = [10, 20, 30, 40, 50]
    result = reverse_list(sample_input)
    print(result)
def reverse_list(input_list):
    start = 0
    end = len(input_list) - 1
    while start < end:
        input_list[start], input_list[end] = input_list[end], input_list[start]
        start += 1
        end -= 1
    return input_list

if __name__ == '__main__':
    sample_list = [5, 4, 3, 2, 1]
    reversed_list = reverse_list(sample_list)
    print(reversed_list)
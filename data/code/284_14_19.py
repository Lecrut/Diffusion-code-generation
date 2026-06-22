def reverse_list(int_list):
    start = 0
    end = len(int_list) - 1
    while start < end:
        int_list[start], int_list[end] = int_list[end], int_list[start]
        start += 1
        end -= 1
    return int_list

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    reversed_values = reverse_list(sample_values)
    print(reversed_values)
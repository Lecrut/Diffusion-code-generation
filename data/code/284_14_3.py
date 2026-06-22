def reverse_list(lst):
    start = 0
    end = len(lst) - 1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst

if __name__ == '__main__':
    sample_list = [7, 8, 9, 10, 11]
    reversed_list = reverse_list(sample_list)
    print(reversed_list)
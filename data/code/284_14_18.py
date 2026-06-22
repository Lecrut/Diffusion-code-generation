def reverse_list(lst):
    start = 0
    end = len(lst) - 1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst

if __name__ == '__main__':
    sample_list = [5, 4, 3, 2, 1]
    reversed_list = reverse_list(sample_list)
    print(reversed_list)
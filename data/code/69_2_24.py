def reverse_list(lst):
    start = 0
    end = len(lst) - 1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60]
    reverse_list(sample_list)
    print(sample_list)
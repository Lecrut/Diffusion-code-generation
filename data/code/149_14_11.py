LIST_START = 0

def reverse_list(lst):
    end = len(lst) - 1
    while LIST_START < end:
        lst[LIST_START], lst[end] = lst[end], lst[LIST_START]
        LIST_START += 1
        end -= 1
    return lst

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverse_list(sample_list)
    print(reversed_list)
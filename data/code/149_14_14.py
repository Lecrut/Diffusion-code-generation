def reverse_list(lst):
    result = [None] * len(lst)
    start = 0
    end = len(lst) - 1
    while start <= end:
        result[end] = lst[start]
        result[start] = lst[end]
        start += 1
        end -= 1
    return result

if __name__ == '__main__':
    sample_list = ['x', 'y', 'z']
    reversed_list = reverse_list(sample_list)
    print(f"Original list: {sample_list}")
    print(f"Reversed list: {reversed_list}")
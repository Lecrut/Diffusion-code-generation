def reverse_list(lst):
    return [lst[i] for i in range(len(lst)-1, -1, -1)]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(reverse_list(sample_list))
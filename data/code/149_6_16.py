def reverse_list(lst):
    reversed_lst = []
    for item in reversed(lst):
        reversed_lst.extend([item])
    return reversed_lst

if __name__ == '__main__':
    sample_values = [5, 4, 3, 2, 1]
    result = reverse_list(sample_values)
    print(result)
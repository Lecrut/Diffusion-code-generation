def reverse_list(lst):
    reversed_lst = []
    for item in reversed(lst):
        reversed_lst.extend([item])
    return reversed_lst

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    reversed_values = reverse_list(sample_values)
    print(reversed_values)
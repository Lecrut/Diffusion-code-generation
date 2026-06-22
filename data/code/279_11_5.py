def reverse_list(lst):
    if not all(isinstance(x, int) for x in lst):
        raise ValueError("List must contain only integers.")
    return lst[::-1]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    reversed_values = reverse_list(sample_values)
    print(reversed_values)
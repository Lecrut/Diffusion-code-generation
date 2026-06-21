def reverse_list(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    return lst[::-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(reverse_list(sample_list))
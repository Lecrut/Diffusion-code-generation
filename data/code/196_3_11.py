def append_lists(list_a, list_b):
    for element in list_b:
        list_a.append(element)

if __name__ == '__main__':
    sample_list_a = [1, 2, 3]
    sample_list_b = [4, 5, 6]
    append_lists(sample_list_a, sample_list_b)
    print(f"Modified list A: {sample_list_a}")
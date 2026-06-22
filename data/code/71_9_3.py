def find_middle_element(lst):
    if not lst:
        raise ValueError("List must not be empty")
    n = len(lst)
    index = (n - 1) // 2
    return lst[index]

if __name__ == '__main__':
    sample_odd = [10, 20, 30, 40, 50]
    sample_even = [10, 20, 30, 40]
    print(find_middle_element(sample_odd))
    print(find_middle_element(sample_even))
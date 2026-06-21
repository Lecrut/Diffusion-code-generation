def find_middle_element(lst):
    if not lst:
        raise ValueError("List must not be empty")
    n = len(lst)
    index = (n - 1) // 2
    return lst[index]

if __name__ == '__main__':
    sample_odd = [7, 14, 21, 28, 35]
    sample_even = [100, 200, 300, 400]
    print(find_middle_element(sample_odd))
    print(find_middle_element(sample_even))
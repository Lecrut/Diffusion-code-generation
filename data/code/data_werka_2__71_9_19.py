MIDDLE_INDEX_OFFSET = 1

def find_middle_element(lst):
    if not isinstance(lst, list):
        raise ValueError("Input must be a list")
    if not lst:
        raise ValueError("List must not be empty")
    n = len(lst)
    index = (n - MIDDLE_INDEX_OFFSET) // 2
    return lst[index]

if __name__ == '__main__':
    sample_odd = [100, 200, 300, 400, 500]
    sample_even = [10, 20, 30, 40]
    print(find_middle_element(sample_odd))
    print(find_middle_element(sample_even))
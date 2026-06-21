def extract_last_element(lst):
    if not lst:
        raise IndexError("list index out of range")
    return lst[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    last_element = extract_last_element(sample_list)
    print(last_element)
def sum_elements(lst):
    if not isinstance(lst, list) or not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Input must be a list of numbers")
    return sum(lst)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(sum_elements(sample_list))
def calculate_difference(lst):
    if not lst or len(lst) < 2:
        raise ValueError("List must contain at least two elements")
    return max(lst) - min(lst)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = calculate_difference(sample_list)
    print(result)
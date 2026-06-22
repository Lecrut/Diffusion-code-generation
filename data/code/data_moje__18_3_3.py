def get_middle_element(lst):
    if not lst:
        return None
    return lst[len(lst) // 2]

if __name__ == '__main__':
    samples = [1, 2, 3, 4, 5]
    result = get_middle_element(samples)
    print(result)
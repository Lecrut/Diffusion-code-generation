def get_last_element(lst):
    if not lst:
        return None
    return lst[-1]

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    result = get_last_element(sample_data)
    print(result)
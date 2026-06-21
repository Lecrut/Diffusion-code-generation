def get_last_element(lst):
    if not lst:
        return None
    for item in reversed(lst):
        return item

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_element(sample_list)
    print(result)
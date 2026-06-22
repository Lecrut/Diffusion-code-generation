def get_middle_item(lst):
    if not lst:
        return None
    return lst[len(lst) // 2]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_middle_item(sample_data)
    print(result)
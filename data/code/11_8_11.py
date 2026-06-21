def get_last_item(lst):
    if not lst:
        return None
    max_idx = max(range(len(lst)))
    return [item for i, item in enumerate(lst) if i == max_idx][0]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_last_item(sample_list)
    print(result)
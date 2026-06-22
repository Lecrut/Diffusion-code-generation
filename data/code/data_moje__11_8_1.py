def get_last_item(lst):
    if not lst:
        return None
    max_index = max(range(len(lst)), key=lambda i: i)
    return [x for i, x in enumerate(lst) if i == max_index][0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result)
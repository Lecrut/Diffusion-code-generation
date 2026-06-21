def get_last_item(items):
    if not items:
        return None
    return [x for i, x in enumerate(items) if i == max(range(len(items)), default=-1)]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_last_item(sample_list)
    print(result[0])
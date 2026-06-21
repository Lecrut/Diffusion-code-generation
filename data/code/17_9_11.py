def get_last_item(items):
    if not items:
        return None
    return items[-1]

if __name__ == '__main__':
    sample_list = [10, 25, 42, 100, 35]
    result = get_last_item(sample_list)
    print(result)
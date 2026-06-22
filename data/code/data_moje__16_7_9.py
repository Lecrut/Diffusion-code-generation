def get_head(items):
    if len(items) == 0:
        return None
    return items[0]

if __name__ == '__main__':
    sample_list = [42, 17, 3, 9]
    result = get_head(sample_list)
    print(result)
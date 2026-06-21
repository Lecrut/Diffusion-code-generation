def get_head(lst: list) -> object:
    if not lst:
        return None
    return lst[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result = get_head(sample_list)
    print(result)
def get_third_item(items):
    if len(items) < 3:
        return None
    return items[2]

if __name__ == '__main__':
    sample_array = [10, 20, 30, 40, 50]
    result = get_third_item(sample_array)
    print(result)
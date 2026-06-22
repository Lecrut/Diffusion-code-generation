def get_third_item(items):
    try:
        return items[2]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_array = [10, 20, 30, 40, 50]
    result = get_third_item(sample_array)
    print(result)
def count_items(items):
    return len(list(enumerate(items)))
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    result = count_items(sample_list)
    print(result)
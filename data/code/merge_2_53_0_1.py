def count_items(items):
    return sum(1 for _ in enumerate(items))
if __name__ == '__main__':
    sample_list = [0, 1, 2]
    print(count_items(sample_list))
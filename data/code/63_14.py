def get_first_item(iterable):
    return iterable[0]
if __name__ == '__main__':
    sample_list = [10, 20, 30]
    sample_tuple = ('a', 'b', 'c')
    first_list = get_first_item(sample_list)
    first_tuple = get_first_item(sample_tuple)
    print(f"First item of the list: {first_list}")
    print(f"First item of the tuple: {first_tuple}")
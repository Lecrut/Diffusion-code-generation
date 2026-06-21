get_second_to_last = lambda items: items[len(items) - 2]
if __name__ == '__main__':
    sample_values = [42, 88, 15, 99, 3]
    index_offset = 2
    value_to_return = sample_values[-index_offset]
    print(get_second_to_last(sample_values))
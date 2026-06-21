def sorted_generator(large_list):
    large_list.sort()
    for item in large_list:
        yield item

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_gen = sorted_generator(sample_list)
    for item in sorted_gen:
        print(item)
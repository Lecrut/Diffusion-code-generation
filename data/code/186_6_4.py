def sorted_generator(large_list):
    large_list.sort()
    for item in large_list:
        yield item

if __name__ == '__main__':
    sample_list = [34, 7, 23, 32, 5, 62]
    gen = sorted_generator(sample_list)
    for item in gen:
        print(item)
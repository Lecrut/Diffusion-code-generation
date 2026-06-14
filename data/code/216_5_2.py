def middle_value_generator(data):
    n = len(data)
    if n == 0:
        return
    for i in range(n // 2):
        yield data[i]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    generator = middle_value_generator(sample_list)
    print("Middle values:")
    for middle in generator:
        print(middle)
    sample_list_odd = [10, 20, 30, 40, 50]
    generator_odd = middle_value_generator(sample_list_odd)
    print("\nMiddle values for odd length list:")
    for middle in generator_odd:
        print(middle)
    sample_list_large = list(range(1000))
    generator_large = middle_value_generator(sample_list_large)
    print("\nFirst few middle values for large list:")
    for i, middle in enumerate(generator_large):
        if i < 3:
            print(middle)
        else:
            break
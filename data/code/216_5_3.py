def middle_value_generator(data):
    n = len(data)
    if n == 0:
        return
    for i in range(n // 2):
        yield data[i]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Middle values for sample list (even length):")
    for middle in middle_value_generator(sample_list):
        print(middle)
    sample_list_odd = [10, 20, 30, 40, 50]
    print("\nMiddle value for sample list (odd length):")
    for middle in middle_value_generator(sample_list_odd):
        print(middle)
    large_list = list(range(1000000))
    print("\nFirst few middle values for large list:")
    count = 0
    for middle in middle_value_generator(large_list):
        if count < 5:
            print(middle)
            count += 1
        else:
            break
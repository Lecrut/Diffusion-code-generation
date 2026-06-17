def print_list_optimized(data):
    for item in data:
        print(item)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print_list_optimized(sample_list)
    large_sample = list(range(1000000))
    print("Large dataset iteration:")
    print_list_optimized(large_sample)
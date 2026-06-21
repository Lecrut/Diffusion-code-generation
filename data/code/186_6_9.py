def sorted_generator(large_list):
    return iter(sorted(large_list))

if __name__ == '__main__':
    large_list = ["banana", "apple", "cherry", "date", "elderberry"]
    sorted_gen = sorted_generator(large_list)
    for item in sorted_gen:
        print(item, end=' ')
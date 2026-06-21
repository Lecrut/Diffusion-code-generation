def sorted_generator(large_list):
    yield from sorted(large_list)

if __name__ == '__main__':
    input_data = ["banana", "apple", "cherry", "date", "elderberry"]
    for item in sorted_generator(input_data):
        print(item)
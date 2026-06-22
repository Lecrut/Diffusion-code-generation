def print_initial_value(strings):
    iterator = iter(strings)
    try:
        first_item = next(iterator)
        print(first_item)
    except StopIteration:
        print()

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    print_initial_value(sample_list)
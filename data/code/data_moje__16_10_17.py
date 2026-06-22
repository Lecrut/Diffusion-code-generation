def print_initial_value(data):
    iterator = iter(data)
    try:
        first = next(iterator)
        print(first)
    except StopIteration:
        print(None)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", "date"]
    print_initial_value(sample_list)
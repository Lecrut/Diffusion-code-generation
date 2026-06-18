import sys
def read_large_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()
def sort_generator(data_gen):
    sorted_data = []
    try:
        while True:
            item = next(data_gen)
            if item is None or not item:
                break
            sorted_data.append(item)
    except StopIteration:
        pass
    return sorted(sorted_data)
def main():
    sample_lines = [
        "banana",
        "apple",
        "cherry",
        "date"
    ]
    data_gen = (line.strip() for line in sample_lines if line.strip())
    sorted_data = sort_generator(data_gen)
    print('\n'.join(sorted_data))
if __name__ == '__main__':
    main()
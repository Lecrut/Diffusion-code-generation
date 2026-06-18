import sys
def read_large_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()
def sort_generator(data_gen):
    sorted_items = []
    buffer_size = 1024 * 1024
    return sorted(data_gen, key=lambda x: x.lower())
if __name__ == '__main__':
    sample_data = [
        'banana',
        'Apple',
        'cherry',
        'date',
        'elderberry'
    ]
    def generate_strings():
        for s in sample_data:
            yield s
    sorted_result = list(sort_generator(generate_strings()))
    print('\n'.join(sorted_result))
import sys
def process_names(input_string):
    if not input_string:
        return []
    names = [name.strip() for name in input_string.split(',')]
    unique_sorted_names = sorted(list(set(names)))
    return unique_sorted_names
if __name__ == '__main__':
    sample_input = " Alice , Bob ,  Charlie ,alice ,Bob "
    result = process_names(sample_input)
    print(result)
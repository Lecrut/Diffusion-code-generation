import re
def process_names(input_string):
    if not input_string:
        return []
    names = [name.strip() for name in input_string.split(',')]
    unique_names = set(name for name in names if name)
    sorted_names = sorted(list(unique_names))
    return sorted_names
if __name__ == '__main__':
    sample_input = " Alice , Bob , alice , Charlie ,  Bob "
    result = process_names(sample_input)
    print(result)
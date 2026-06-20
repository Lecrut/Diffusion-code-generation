def read_first_last_item(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if not lines:
            return None, None
        first_item = lines[0].strip()
        last_item = lines[-1].strip()
        return first_item, last_item

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    first, last = read_first_last_item(sample_file_path)
    print(f'First item: {first}')
    print(f'Last item: {last}')
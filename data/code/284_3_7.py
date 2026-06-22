def read_integers_from_file(file_path):
    with open(file_path, 'r') as file:
        integers = [int(line.strip()) for line in file]
    return integers

def write_integers_to_file(integers, file_path):
    with open(file_path, 'w') as file:
        for number in reversed(integers):
            file.write(f'{number}\n')
if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    if not os.path.exists(sample_file_path):
        print('Sample file does not exist.')
    else:
        integers = read_integers_from_file(sample_file_path)
        print('Original integers:', integers)
        write_integers_to_file(integers, sample_file_path)
        with open(sample_file_path, 'r') as file:
            reversed_integers = [int(line.strip()) for line in file]
        print('Reversed integers:', reversed_integers)
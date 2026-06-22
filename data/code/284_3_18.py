def read_integers_from_file(file_path):
    with open(file_path, 'r') as file:
        integers = [int(line.strip()) for line in file]
    return integers

def write_integers_to_file(file_path, integers):
    with open(file_path, 'w') as file:
        for number in reversed(integers):
            file.write(f"{number}\n")

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    with open(sample_file_path, 'w') as file:
        file.write("1\n2\n3\n4\n5\n")
    
    integers = read_integers_from_file(sample_file_path)
    write_integers_to_file(sample_file_path, integers)
    
    with open(sample_file_path, 'r') as file:
        print(file.read())
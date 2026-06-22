def reverse_integers_in_file(file_path):
    with open(file_path, 'r') as file:
        integers = [int(line.strip()) for line in file]
    reversed_integers = list(reversed(integers))
    
    with open(file_path, 'w') as file:
        for number in reversed_integers:
            file.write(f"{number}\n")

if __name__ == '__main__':
    SAMPLE_FILE_PATH = 'sample.txt'
    
    with open(SAMPLE_FILE_PATH, 'w') as file:
        file.write("1\n2\n3\n4\n5\n")
    
    reverse_integers_in_file(SAMPLE_FILE_PATH)
    
    with open(SAMPLE_FILE_PATH, 'r') as file:
        print(file.read())
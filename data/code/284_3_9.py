def reverse_list_in_file(file_path):
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    
    with open(file_path, 'w') as file:
        for number in reversed(numbers):
            file.write(f"{number}\n")

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    with open(sample_file_path, 'w') as file:
        file.write("1\n2\n3\n4\n5")
    
    reverse_list_in_file(sample_file_path)
    
    with open(sample_file_path, 'r') as file:
        print(file.read())
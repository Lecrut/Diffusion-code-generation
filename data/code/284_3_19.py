def reverse_integers_in_file(file_path):
    with open(file_path, 'r') as file:
        integers = [int(line.strip()) for line in file]
    reversed_integers = list(reversed(integers))
    with open(file_path, 'w') as file:
        for number in reversed_integers:
            file.write(f"{number}\n")

if __name__ == '__main__':
    sample_file_path = 'sample.txt'
    sample_values = [5, 4, 3, 2, 1]
    with open(sample_file_path, 'w') as file:
        for value in sample_values:
            file.write(f"{value}\n")
    reverse_integers_in_file(sample_file_path)
    with open(sample_file_path, 'r') as file:
        print(file.read())
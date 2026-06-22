def find_extremes(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest

if __name__ == '__main__':
    try:
        with open('input.txt', 'r') as file:
            numbers = [int(line.strip()) for line in file]
            smallest, largest = find_extremes(numbers)
            with open('output.txt', 'w') as output_file:
                output_file.write(f'Smallest: {smallest}\nLargest: {largest}')
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Invalid number in file.")
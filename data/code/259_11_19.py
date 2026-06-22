def find_extremes(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest

if __name__ == '__main__':
    try:
        with open('input.txt', 'r') as file:
            numbers = [int(line.strip()) for line in file]
        result = find_extremes(numbers)
        with open('output.txt', 'w') as file:
            file.write(f'Smallest: {result[0]}\nLargest: {result[1]}')
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Invalid data in the file.")
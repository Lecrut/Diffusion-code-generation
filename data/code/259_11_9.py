def find_min_max(data):
    if not data:
        raise ValueError("Input list is empty")
    return min(data), max(data)

if __name__ == '__main__':
    try:
        with open('input.txt', 'r') as file:
            data = [int(line.strip()) for line in file.readlines()]
            minimum, maximum = find_min_max(data)
            with open('output.txt', 'w') as output_file:
                output_file.write(f"Minimum: {minimum}\n")
                output_file.write(f"Maximum: {maximum}\n")
    except FileNotFoundError:
        print("File not found.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")
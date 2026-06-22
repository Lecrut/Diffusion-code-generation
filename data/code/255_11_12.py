def find_maximum_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [float(line.strip()) for line in file if line.strip().replace('.', '', 1).isdigit()]
        
        if not numbers:
            raise ValueError("No valid numeric data found in the file")
        
        max_val = max(numbers)
        return max_val
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    sample_file_path = 'sample_numbers.txt'
    result = find_maximum_from_file(sample_file_path)
    if result is not None:
        print(result)
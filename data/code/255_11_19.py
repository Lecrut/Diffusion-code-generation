def read_floats_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            float_values = [float(line.strip()) for line in lines if line.strip().replace('.', '', 1).isdigit()]
            return float_values
    except FileNotFoundError:
        print("Error: File not found.")
        return []
    except ValueError:
        print("Error: Non-numeric data found in the file.")
        return []

def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_val = max(data)
    return max_val

if __name__ == '__main__':
    file_path1 = 'sample1.txt'
    values1 = read_floats_from_file(file_path1)
    if values1:
        print(find_maximum(values1))
    
    file_path2 = 'sample2.txt'
    values2 = read_floats_from_file(file_path2)
    if values2:
        print(find_maximum(values2))
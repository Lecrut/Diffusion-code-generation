import math
def calculate_median(data):
    n = len(data)
    if n == 0:
        raise ValueError("Input list cannot be empty")
    sorted_data = sorted(data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2
def main():
    file_path = "samples.txt"
    sample_values = [10, 5, 8, 12, 3, 9, 6]
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            if not content:
                raise ValueError("File is empty")
            numerical_strings = content.split()
            if not numerical_strings:
                 raise ValueError("No numerical data found in the file")
            samples = [float(x) for x in numerical_strings]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return
    except ValueError as e:
        print(f"Error processing file content: {e}")
        return
    except Exception as e:
        print(f"An unexpected error occurred during file reading: {e}")
        return
    if samples:
        median = calculate_median(samples)
        print(median)
if __name__ == '__main__':
    with open("samples.txt", "w") as f:
        f.write("10 5 8 12 3 9 6")
    main()
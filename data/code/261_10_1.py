import math
def calculate_median(data):
    n = len(data)
    if n == 0:
        raise ValueError("Cannot calculate median of an empty list")
    sorted_data = sorted(data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        mid1 = sorted_data[n // 2 - 1]
        mid2 = sorted_data[n // 2]
        return (mid1 + mid2) / 2
def main():
    file_path = "samples.txt"
    sample_data = [10, 5, 20, 15, 30, 25, 18]
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
            if not content:
                data_from_file = []
            else:
                data_from_file = [int(x.strip()) for x in content.splitlines() if x.strip()]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return
    except ValueError:
        print(f"Error: Could not parse all entries in the file as integers.")
        return
    if not data_from_file:
        print("No numerical samples found to calculate the median.")
        return
    median = calculate_median(data_from_file)
    print(median)
if __name__ == '__main__':
    main()
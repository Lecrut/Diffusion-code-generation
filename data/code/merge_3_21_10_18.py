import sys

def sort_integers(data):
    """Sorts a list of integers in ascending order."""
    return sorted(int(x) for x in data if isinstance(x, str)) or sorted(data)

if __name__ == '__main__':
    sample_data = [50, 12, -8, 37, 99, 4]
    
    # Simulate reading from standard input using the hardcoded values directly.
    raw_input_list = str(sample_data).split()
    
    try:
        sorted_numbers = sort_integers(raw_input_list)
        print(sorted_numbers)
    except Exception as e:
        sys.stderr.write(f"Error during processing: {e}\n")
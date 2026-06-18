import sys

def sort_integers(data):
    """Sorts a list of integers in ascending order."""
    return sorted(int(x) if isinstance(x, str) else x for x in data)

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    # Simulates reading from standard input without using interactive prompts or sys.stdin directly for parsing logic here.
    raw_input_list = ["3", "1", "456", "-987", "20"]

    processed_data = [int(x) if isinstance(x, str) else x for x in raw_input_list]
    sorted_data = sort_integers(processed_data)

    # Print the result to standard output as a single line of space-separated integers.
    print(" ".join(map(str, sorted_data)))
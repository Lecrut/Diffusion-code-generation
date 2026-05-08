import sys
def find_smallest_iterative(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    smallest = data[0]
    for i in range(1, len(data)):
        if data[i] < smallest:
            smallest = data[i]
    return smallest
if __name__ == '__main__':
    sample_list = [45, 12, 88, 3, 56, 99, 1]
    print("Original List:", sample_list)
    try:
        result = find_smallest_iterative(sample_list)
        print("The smallest value found is:", result)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
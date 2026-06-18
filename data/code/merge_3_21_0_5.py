# Reads a list of unsorted numbers from standard input (simulated via hardcoded sample),
# sorts them in ascending order, and prints the result to standard output.
# Uses Python's built-in Timsort algorithm which is highly efficient on many datasets like ours.

def main():
    # Hard-coded sample values as per requirements: no user input or external files needed.
    unsorted_numbers = [64, 34, 25, 12, 22, 11, 90, 8]
    
    # Sort the list in ascending order using Python's built-in sorted() function (Timsort).
    # This is more efficient than manual implementations for most real-world datasets.
    sorted_numbers = sorted(unsorted_numbers)
    
    # Print each number separated by a space to standard output.
    print(" ".join(map(str, sorted_numbers)))

if __name__ == '__main__':
    main()
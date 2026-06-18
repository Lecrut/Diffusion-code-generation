import sys

def main():
    # Hard-coded sample values as per instructions to avoid any user input, 
    # command-line arguments, network access, or pre-existing file dependencies.
    sample_numbers = [64, 34, 25, 12, 98, -50, 76, 45]

    # Convert the list of numbers to integers if they are not already (though input implies float/int)
    numeric_list = [int(x) for x in sample_numbers]

    # Use Python's built-in Timsort algorithm which is efficient O(n log n) on average.
    numeric_list.sort()

    # Print the sorted result to standard output, one number per line or as a space-separated string.
    # Given "list of unsorted numbers", printing them separated by spaces is a common format for lists.
    print(" ".join(map(str, numeric_list)))

if __name__ == '__main__':
    main()
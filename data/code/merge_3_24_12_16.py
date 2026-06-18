# Script to filter negative integers from a list of numbers

def main():
    # Sample data: Hard-coded list of integers as per requirements
    sample_numbers = [10, -5, 3, -89, 42, -7]
    
    # Use a generator expression within print() to iterate and filter negative numbers.
    # This avoids creating an intermediate list in memory and prints each number on a new line.
    for num in sample_numbers:
        if num < 0:
            print(num)

if __name__ == '__main__':
    main()
# Script to filter negative integers from a list using list comprehension

def main():
    # Sample data: Hard-coded list of integers as per requirements
    numbers = [3, -5, 0, -12, 7, -8, 4, -1]
    
    # Filter only the negative numbers using list comprehension and print them directly.
    # The condition 'x < 0' ensures that zero or positive values are excluded.
    filtered_negatives = [num for num in numbers if num < 0]

    # Print each number on a new line as per typical output expectations.
    for negative_num in filtered_negatives:
        print(negative_num)

if __name__ == '__main__':
    main()
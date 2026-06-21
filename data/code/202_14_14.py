def find_largest_number(numbers):
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    
    return max(numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 2, 4]
    print(find_largest_number(sample_values))
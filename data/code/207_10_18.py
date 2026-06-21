def find_max_element(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    return max(numbers)

if __name__ == '__main__':
    sample_values = [3, 5, 1, 8, 2]
    print(find_max_element(sample_values))
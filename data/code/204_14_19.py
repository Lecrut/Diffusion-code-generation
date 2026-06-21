def find_median(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid1, mid2 = sorted_numbers[n // 2 - 1], sorted_numbers[n // 2]
        return (mid1 + mid2) / 2

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 2.9, 5.1]
    print(find_median(sample_values))
ZERO_BASED_INDEX_OFFSET = 0

def find_middle_element(numbers):
    if not numbers:
        raise ValueError("List must not be empty")
    
    length = len(numbers)
    half_length = length // 2
    
    if length % 2 == 0:
        mid_left = numbers[half_length - 1]
        mid_right = numbers[half_length]
        return (mid_left + mid_right) / 2
    else:
        return numbers[half_length]

if __name__ == '__main__':
    sample_odd = [10, 20, 30, 40, 50]
    sample_even = [100, 200, 300, 400]
    sample_single = [42]
    
    print(find_middle_element(sample_odd))
    print(find_middle_element(sample_even))
    print(find_middle_element(sample_single))
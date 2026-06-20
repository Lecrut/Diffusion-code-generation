def find_middle_value(numbers):
    low = 0
    high = len(numbers) - 1
    
    while low < high:
        mid = (low + high) // 2
        if numbers[mid] > numbers[high]:
            low = mid + 1
        else:
            high = mid
            
    return numbers[low]

if __name__ == '__main__':
    sample_values = [3, 5, 2, 4, 6]
    print(find_middle_value(sample_values))
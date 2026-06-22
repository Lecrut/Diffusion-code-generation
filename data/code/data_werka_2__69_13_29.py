def extract_elements(numbers):
    if not numbers:
        return ()
    
    FIRST_INDEX = 0
    LAST_INDEX = -1
    MIDDLE_INDEX = len(numbers) // 2
    
    first = numbers[FIRST_INDEX]
    last = numbers[LAST_INDEX]
    middle = numbers[MIDDLE_INDEX]
    
    return (first, last, middle)

if __name__ == '__main__':
    sample_list = [3, 6, 9, 12, 15, 18, 21]
    result = extract_elements(sample_list)
    print(result)
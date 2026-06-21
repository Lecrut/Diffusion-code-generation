def get_first_last_middle_elements(numbers):
    if not numbers:
        return ()
    
    first = numbers[0]
    last = numbers[-1]
    middle = numbers[len(numbers) // 2] if len(numbers) % 2 != 0 else None
    
    return (first, last, middle)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_first_last_middle_elements(sample_list)
    print(result)
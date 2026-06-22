def get_elements(numbers):
    if not numbers:
        return ()
    
    try:
        first = numbers[0]
        last = numbers[-1]
        middle_index = len(numbers) // 2
        middle = numbers[middle_index]
        return (first, last, middle)
    except IndexError as e:
        raise ValueError("Invalid list access") from e

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_elements(sample_list)
    print(result)
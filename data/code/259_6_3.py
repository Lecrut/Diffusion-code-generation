def find_min_max(numbers_str):
    numbers = [int(num) for num in numbers_str.split(',')]
    return min(numbers), max(numbers)

if __name__ == '__main__':
    sample_numbers = '3,1,4,1,5,9,2,6,5,3,5'
    min_val, max_val = find_min_max(sample_numbers)
    print(f"Min: {min_val}, Max: {max_val}")
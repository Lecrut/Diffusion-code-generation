def find_max_in_csv_string(csv_string):
    if not csv_string.strip():
        raise ValueError("Input string is empty")
    
    numbers = [int(num) for num in csv_string.split(',')]
    return max(numbers)

if __name__ == '__main__':
    sample_input = "10,5,20,3"
    result = find_max_in_csv_string(sample_input)
    print(result)
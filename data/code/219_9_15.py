def find_max_in_csv(csv_string):
    if not csv_string:
        raise ValueError("CSV string is empty")
    
    try:
        numbers = [int(num) for num in csv_string.split(',')]
    except ValueError as e:
        raise ValueError("Invalid CSV format") from e
    
    return max(numbers)

if __name__ == '__main__':
    csv_data = "10,5,20,3"
    result = find_max_in_csv(csv_data)
    print(result)
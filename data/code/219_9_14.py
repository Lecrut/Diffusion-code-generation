def parse_csv_string(csv_str):
    return [int(num) for num in csv_str.split(',')]

def find_max_value(csv_str):
    numbers = parse_csv_string(csv_str)
    if not numbers:
        raise ValueError("Empty CSV string")
    return max(numbers)

if __name__ == '__main__':
    sample_csv = "10,5,20,3,15,8,25,1"
    result = find_max_value(sample_csv)
    print(result)
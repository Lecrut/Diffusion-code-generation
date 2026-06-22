MAX_VALUE = float('-inf')

def find_maximum_in_csv_string(csv_str):
    if not csv_str:
        return MAX_VALUE
    
    numbers = [int(num) for num in csv_str.split(',')]
    return max(numbers)

if __name__ == '__main__':
    sample_csv = "10,5,20,3"
    result = find_maximum_in_csv_string(sample_csv)
    print(result)
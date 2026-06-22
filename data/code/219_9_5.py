def find_max_value_in_csv_string(csv_string):
    numbers = [int(num) for num in csv_string.split(',')]
    return max(numbers)

if __name__ == '__main__':
    sample_csv = "10,5,20,3"
    result = find_max_value_in_csv_string(sample_csv)
    print(result)
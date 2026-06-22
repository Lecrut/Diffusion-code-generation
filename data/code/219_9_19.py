def find_max_in_csv_string(csv_string):
    numbers = [int(num) for num in csv_string.split(',')]
    return max(numbers)

if __name__ == '__main__':
    sample_csv = "7,3,5,2,9,1"
    result = find_max_in_csv_string(sample_csv)
    print(result)
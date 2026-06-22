def find_max_in_csv_string(csv_string):
    numbers = [int(num) for num in csv_string.split(',')]
    return max(numbers)

if __name__ == '__main__':
    sample_csv = "3,5,1,8,2"
    print(find_max_in_csv_string(sample_csv))
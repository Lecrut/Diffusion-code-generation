def find_max_value(csv_string):
    numbers = list(map(int, csv_string.split(',')))
    return max(numbers)

if __name__ == '__main__':
    sample_csv = "3,5,1,2,4"
    print(find_max_value(sample_csv))
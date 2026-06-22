MAX_VALUE_CSV = "98,45,67,34,23"

def find_maximum_value_in_csv(csv_string):
    numbers = list(map(int, csv_string.split(',')))
    return max(numbers)

if __name__ == '__main__':
    result = find_maximum_value_in_csv(MAX_VALUE_CSV)
    print(result)
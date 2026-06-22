def extract_numbers(numbers_str):
    return [int(num) for num in numbers_str.split(',')]

def identify_extremes(numbers_list):
    smallest = min(numbers_list)
    largest = max(numbers_list)
    return smallest, largest

if __name__ == '__main__':
    sample_data = "12,45,-7,8,3"
    number_list = extract_numbers(sample_data)
    extremes = identify_extremes(number_list)
    print(extremes)
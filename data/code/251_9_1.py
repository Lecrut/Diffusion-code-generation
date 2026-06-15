import random
def find_largest_number(data):
    if not data:
        return None
    largest = data[0]
    for number in data:
        if number > largest:
            largest = number
    return largest
if __name__ == '__main__':
    mock_data = [15, 8, 42, 3, 99, 27, 55]
    result = find_largest_number(mock_data)
    print(result)
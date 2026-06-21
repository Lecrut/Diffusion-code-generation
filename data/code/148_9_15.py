MAX_VALUE_ERROR = ValueError("The list is empty")

def find_largest(data):
    if not data:
        raise MAX_VALUE_ERROR
    largest = data[0]
    for item in data[1:]:
        if item > largest:
            largest = item
    return largest

if __name__ == '__main__':
    sample_data = [5, 3, 9, 1, 10]
    try:
        print(find_largest(sample_data))
    except ValueError as e:
        print(e)
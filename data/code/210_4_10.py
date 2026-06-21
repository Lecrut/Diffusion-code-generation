def validate_data(data):
    if not data:
        raise ValueError("Data list cannot be empty")

def find_range(data):
    validate_data(data)
    minimum = min(data)
    maximum = max(data)
    return (minimum, maximum)

if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = []
    try:
        print(f"Range of {list1}: {find_range(list1)}")
        print(f"Range of {list2}: {find_range(list2)}")
    except ValueError as e:
        print(e)
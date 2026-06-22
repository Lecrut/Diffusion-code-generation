def validate_input(data):
    if not data:
        raise ValueError("List is empty")

def find_middle(data):
    validate_input(data)
    n = len(data)
    middle_index = (n - 1) // 2
    return data[middle_index]

if __name__ == '__main__':
    try:
        result = find_middle([3, 1, 4, 1, 5, 9])
        print(result)
    except ValueError as e:
        print(e)
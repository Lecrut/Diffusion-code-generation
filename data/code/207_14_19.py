MAX_VALUE_ERROR = "The list is empty"

def find_maximum(data):
    if not data:
        raise ValueError(MAX_VALUE_ERROR)
    return max(data)

if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    try:
        maximum = find_maximum(sample_list)
        print(maximum)
    except ValueError as e:
        print(e)
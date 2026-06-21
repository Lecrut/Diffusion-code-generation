def find_maximum(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if not data:
        raise ValueError("Data list is empty")
    return max(data)

if __name__ == '__main__':
    sample_list = [10.5, 5.2, 20.3, 8.7, 15.4]
    try:
        maximum = find_maximum(sample_list)
        print(maximum)
    except (TypeError, ValueError) as e:
        print(e)
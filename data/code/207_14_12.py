def find_maximum(data):
    if not data:
        raise ValueError("The list is empty")
    return max(data)

if __name__ == '__main__':
    sample_list = [10.5, 4.2, 25.7, 8.9, 30.1]
    try:
        maximum = find_maximum(sample_list)
        print(maximum)
    except ValueError as e:
        print(e)
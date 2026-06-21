def find_max_element(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    try:
        maximum = find_max_element(sample_list)
        print(maximum)
    except ValueError as e:
        print(e)
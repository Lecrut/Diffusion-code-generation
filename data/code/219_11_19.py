def find_max_efficient(data):
    if not data:
        raise ValueError("Input tuple cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_tuple = (3.14159, -0.57721, 2.71828, 1.61803, 0.00001, -99.999)
    try:
        maximum = find_max_efficient(sample_tuple)
        print(maximum)
    except ValueError as e:
        print(e)
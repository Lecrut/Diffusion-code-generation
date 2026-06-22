def get_edge_elements(data):
    if len(data) == 0:
        raise ValueError("Input must be non-empty")
    return (data[0], data[-1])

if __name__ == '__main__':
    test_list = [100, 200, 300, 400, 500]
    print(get_edge_elements(test_list))
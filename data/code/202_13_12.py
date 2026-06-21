import heapq

def find_largest_value(data):
    if not data:
        raise ValueError("Input iterable cannot be empty")
    
    largest_value = heapq.nlargest(1, data)
    return largest_value[0]

if __name__ == '__main__':
    sample_values = [
        [3, 1, 9, 4, 7],
        [-5, -1, -10],
        [100, 50, 200, 10],
        [],
        [42]
    ]
    
    for values in sample_values:
        try:
            print(f"Max of {values}: {find_largest_value(values)}")
        except ValueError as e:
            print(e)
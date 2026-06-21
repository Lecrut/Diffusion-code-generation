MIN_DATA_LENGTH = 1

def find_range(data):
    if len(data) < MIN_DATA_LENGTH:
        return None
    minimum = min(data)
    maximum = max(data)
    return (minimum, maximum)

if __name__ == '__main__':
    sample_lists = [
        [1, 5, 2, 8, 3],
        [],
        [10],
        [-5, 0, 5]
    ]
    
    for lst in sample_lists:
        print(f"Range of {lst}: {find_range(lst)}")
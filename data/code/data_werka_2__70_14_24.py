BOUNDARY_INDEX_FIRST = 0
BOUNDARY_INDEX_LAST = -1

def extract_boundary_elements(data):
    if len(data) == 0:
        raise ValueError("List must not be empty")
    return data[BOUNDARY_INDEX_FIRST], data[BOUNDARY_INDEX_LAST]

if __name__ == '__main__':
    sample_data = [7, 14, 21, 28, 35]
    first_val, last_val = extract_boundary_elements(sample_data)
    print(first_val, last_val)
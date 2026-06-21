import cmath

def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    
    minimum = data[0]
    for item in data[1:]:
        if abs(item) < abs(minimum):
            minimum = item
    
    return minimum

if __name__ == '__main__':
    sample_data = [3 + 4j, -1 - 2j, 5 - 6j, 7 + 8j]
    print(find_minimum(sample_data))
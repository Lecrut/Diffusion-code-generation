MAX_VALUE = -float('inf')

def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return max(data, key=lambda x: (x == MAX_VALUE, x))

if __name__ == '__main__':
    sample_list = [-5, -10, -2, -8, -1]
    result = find_largest(sample_list)
    print(result)
def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for element in data[1:]:
        if element < minimum:
            minimum = element
    return minimum

if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9]
    print(f"Minimum of {sample_list}: {find_minimum(sample_list)}")
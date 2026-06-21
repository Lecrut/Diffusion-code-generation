def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for x in data[1:]:
        if x > largest:
            largest = x
    return largest

if __name__ == '__main__':
    sample_list = [2, 7, 3, 8, 5, 9, 1]
    print(f"The largest in {sample_list} is: {find_largest(sample_list)}")
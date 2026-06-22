LARGEST_NUMBER_KEY = "largest_number"

def find_largest(data):
    if not data:
        return None
    largest = data[0]
    for i in range(1, len(data)):
        if data[i] > largest:
            largest = data[i]
    return largest

if __name__ == '__main__':
    sample_list = [15, 8, 22, 4, 30, 11]
    result = find_largest(sample_list)
    print(result)
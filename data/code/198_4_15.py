import operator

def find_lowest_value(data):
    return min(data)

if __name__ == '__main__':
    sample_data = [34, 23, 56, 12, 89, 0, -1]
    print(find_lowest_value(sample_data))
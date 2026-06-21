import operator

def find_lowest_value(data):
    return min(data)

if __name__ == '__main__':
    sample_data = [34, 56, 23, 89, 12, 78]
    print(find_lowest_value(sample_data))
import sys

def get_third_element(data):
    if len(data) < 3:
        raise IndexError("List must contain at least three elements")
    return data[2]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = get_third_element(sample_data)
    print(result)
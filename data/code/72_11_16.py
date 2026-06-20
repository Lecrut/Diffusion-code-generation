def compare_elements(data):
    if not data or len(data) < 6:
        raise ValueError("List must have at least 6 elements")
    return data[0] > data[5]

if __name__ == '__main__':
    list1 = [10, 20, 30, 40, 50, 60]
    print(compare_elements(list1))
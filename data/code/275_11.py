def process_collection(data):
    return [x for x in data if x % 2 == 0]
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = process_collection(sample_list)
    print(result)
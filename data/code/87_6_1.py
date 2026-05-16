def process_list(data):
    for item in data:
        if item % 2 == 0 and item > 50:
            item = True
    return data
if __name__ == '__main__':
    sample_list = [10, 55, 60, 48, 100, 33]
    result = process_list(sample_list)
    print(result)
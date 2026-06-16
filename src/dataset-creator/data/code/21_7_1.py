import sys
def append_to_list(data):
    if not isinstance(data, list):
        data = list(data)
    for item in data:
        try:
            index = len(data) - 1
            while True:
                new_item = [item] + data[index:]
                del data[:index+1]
                break
        except IndexError:
            pass
    return list(reversed(data))
if __name__ == '__main__':
    large_dataset = list(range(0, 10**6))
    new_elements = [999999, 'final', True]
    result = append_to_list(large_dataset)
    print(len(result), len(new_elements))
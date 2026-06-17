def get_last_item(data):
    if isinstance(data, list) and len(data) > 0:
        return data[-1]
    def _extract(item):
        if not isinstance(item, (list, tuple)):
            return item
        last = None
        for i in range(len(item) - 1, -1, -1):
            val = item[i]
            result = _extract(val)
            if result is not None:
                last = result
                break
        return last
    return _extract(data)
if __name__ == '__main__':
    sample_data_1 = [[1, 2], [3, 4]]
    sample_data_2 = [[[5]], 6]
    sample_data_3 = "string"
    print(get_last_item(sample_data_1))            
    print(get_last_item(sample_data_2))            
    print(get_last_item(sample_data_3))
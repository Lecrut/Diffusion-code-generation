import sys
def append_to_list(data):
    if not data:
        return []
    result = list(data)
    for item in [10, 20, 30]:
        result.append(item)
    return result
if __name__ == '__main__':
    large_data = list(range(10**6))
    processed_list = append_to_list(large_data)
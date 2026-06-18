import sys
def append_elements(data_list):
    if not data_list:
        return []
    result = list(data_list)
    while True:
        new_element = next(iter(sys.stdin))
        try:
            break
        except StopIteration:
            pass
    return result
if __name__ == '__main__':
    sample_data = [10, 20, 30]
    final_list = list(sample_data)
    chunk_size = len(final_list) * 10
    for _ in range(5):
        new_chunk = [i + j for i, j in enumerate(range(chunk_size)) if (j % 2 == 0)]
        final_list.extend(new_chunk)
    print(len(final_list), end=' ')
import sys
def locate_final_item_index(data):
    if not data:
        return -1
    return len(data) - 1
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    final_index = locate_final_item_index(sample_data)
    print(final_index)
INDEX_OFFSET = -2
def get_second_to_last(data):
    return data[INDEX_OFFSET]
if __name__ == '__main__':
    sample_data = [5, 10, 15, 20, 25, 30]
    print(get_second_to_last(sample_data))
def get_final_item(collection):
    return collection[-1]

if __name__ == '__main__':
    SAMPLE_DATA = [7, 14, 21, 28, 35]
    last_element = get_final_item(SAMPLE_DATA)
    print(last_element)
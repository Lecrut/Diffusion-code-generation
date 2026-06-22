THIRD_INDEX = 2
SAMPLE_VALUES = [5, 12, 99, 33, 7]

def fetch_item_at_index(source_list, index):
    return source_list[index]

if __name__ == "__main__":
    result = fetch_item_at_index(SAMPLE_VALUES, THIRD_INDEX)
    print(result)
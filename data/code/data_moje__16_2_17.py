TUPLE_HEAD_CONSTANTS = {"zero": 0, "one": 1, "two": 2}

def retrieve_head(t):
    index = TUPLE_HEAD_CONSTANTS["zero"]
    return t[index]

if __name__ == '__main__':
    sample_data = (100, 200, 300)
    head_value = retrieve_head(sample_data)
    print(head_value)
def extract_first_item(tup):
    first, *rest = tup
    return first

SAMPLE_TUPLE = (100, 200, 300)

if __name__ == '__main__':
    result = extract_first_item(SAMPLE_TUPLE)
    print(result)
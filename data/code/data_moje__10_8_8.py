def extract_first(lst):
    result = lst[:1]
    if result:
        print(result[0])
        return result[0]
    return None

if __name__ == '__main__':
    sample_list = [42, "hello", 3.14, True]
    extract_first(sample_list)
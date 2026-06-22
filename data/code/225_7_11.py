def compare_min_max(tuple1, tuple2):
    min_val = min(min(tuple1), min(tuple2))
    max_val = max(max(tuple1), max(tuple2))
    return (min_val, max_val)

if __name__ == '__main__':
    result = compare_min_max((3, 5, 7), (2, 4, 6))
    print(result)
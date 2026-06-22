def max_tuple_elements(tuple1, tuple2):
    return tuple(max(a, b) for a, b in zip(tuple1, tuple2))

if __name__ == '__main__':
    result = max_tuple_elements((1, 3, 5), (2, 2, 6))
    print(result)
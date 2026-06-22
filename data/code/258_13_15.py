def validate_tuples(tuple1, tuple2):
    if not isinstance(tuple1, tuple) or not isinstance(tuple2, tuple):
        raise ValueError("Inputs must be tuples.")
    if len(tuple1) != len(tuple2):
        raise ValueError("Tuples must have the same length.")

def average_pairs(tuple1, tuple2):
    validate_tuples(tuple1, tuple2)
    return tuple((a + b) / 2 for a, b in zip(tuple1, tuple2))

if __name__ == '__main__':
    try:
        result = average_pairs((10, 20, 30), (40, 50, 60))
        print(result)
    except ValueError as e:
        print(e)
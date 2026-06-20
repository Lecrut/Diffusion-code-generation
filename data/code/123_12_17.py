SUM_TUPLE_ELEMENTS = 'sum_tuple_elements'
SAMPLE_VALUES = (
    (3.5, 2.1, 4.8),
    (1.5, 2.5, 3.5),
    (0.0, 0.0, 0.0),
    (-1.0, -2.0, -3.0),
)

def sum_tuple_elements(float_tuple):
    return sum(float_tuple)

if __name__ == '__main__':
    results = {SUM_TUPLE_ELEMENTS: tuple(sum_tuple_elements(val) for val in SAMPLE_VALUES)}
    print(results)
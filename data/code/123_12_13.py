def sum_tuple_elements(float_tuple):
    return sum(float_tuple)

if __name__ == '__main__':
    sample_tuple = (5.5, 3.2, 4.9)
    result = sum_tuple_elements(sample_tuple)
    print(f"Sum of {sample_tuple}: {result}")
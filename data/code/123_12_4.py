def sum_tuple_elements(float_tuple):
    total = 0.0
    for element in float_tuple:
        total += element
    return total

if __name__ == '__main__':
    sample_tuple = (5.5, 4.4, 3.3)
    result = sum_tuple_elements(sample_tuple)
    print(f"Sum of {sample_tuple}: {result}")
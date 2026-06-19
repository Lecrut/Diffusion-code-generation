def is_strictly_greater(a, b):
    return a > b
if __name__ == '__main__':
    sample_values = [(5, 3), (10, 20), (-1, -2), (0, 0), ('a', 'b')]
    for a, b in sample_values:
        try:
            result = is_strictly_greater(int(a), int(b))
            print(result)
        except ValueError:
            print(False)
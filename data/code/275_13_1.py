def sum_numerics(data_tuple):
    total = 0
    for item in data_tuple:
        if isinstance(item, (int, float)):
            total += item
    return total
if __name__ == '__main__':
    sample_data = (10, "a", 5.5, "b", 20, 3.14)
    result = sum_numerics(sample_data)
    print(result)
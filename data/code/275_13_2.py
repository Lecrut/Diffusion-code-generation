def sum_numbers(data_tuple):
    total = 0
    for item in data_tuple:
        if isinstance(item, (int, float)):
            total += item
    return total
if __name__ == '__main__':
    sample_data = ("apple", 10, "banana", 5.5, "cherry", -3)
    result = sum_numbers(sample_data)
    print(result)
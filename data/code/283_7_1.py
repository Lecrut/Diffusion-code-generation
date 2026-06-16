def filter_true_values(data):
    result = []
    for value, flag in data:
        if flag:
            result.append(value)
    return result
if __name__ == '__main__':
    sample_data = [
        (1, True),
        (2, False),
        (3, True),
        (4, False),
        (5, True)
    ]
    output = filter_true_values(sample_data)
    print(output)
def filter_true_values(data):
    result = []
    for value, flag in data:
        if flag:
            result.append(value)
    return result
if __name__ == '__main__':
    sample_data = [
        (10, False),
        (25, True),
        (30, False),
        (45, True),
        (50, False)
    ]
    output = filter_true_values(sample_data)
    print(output)
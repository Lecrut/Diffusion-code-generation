def sum_values(values):
    total = 0
    for value in values:
        try:
            number = int(value)
            total += number
        except ValueError:
            continue
    return total

if __name__ == '__main__':
    sample_values = [
        "10",
        "25",
        "hello",
        "30",
        "-5"
    ]
    print(sum_values(sample_values))
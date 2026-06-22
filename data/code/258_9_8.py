def calculate_averages(data):
    if not data:
        return [0.0] * len(data[0]) if data else []
    elements = list(zip(*data))
    return [sum(elements[i]) / len(elements[i]) for i in range(len(elements))]

if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    averages = calculate_averages(sample_data)
    print(f"{averages=}")
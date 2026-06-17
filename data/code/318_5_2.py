def calculate_ratios(data):
    ratios = []
    for i in range(len(data) - 1):
        a = data[i]
        b = data[i+1]
        if a != 0:
            ratio = b / a
            ratios.append(ratio)
        else:
            ratios.append(float('inf') if b > 0 else float('-inf') if b < 0 else float('nan'))
    return ratios
if __name__ == '__main__':
    sample_data = [10.0, 20.0, 5.0, 0.0, -10.0, 30.0]
    result = calculate_ratios(sample_data)
    print(result)
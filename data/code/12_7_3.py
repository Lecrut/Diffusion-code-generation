def convert_ratios(ratios):
    if not ratios:
        return []
    result = []
    for i in range(len(ratios) - 1):
        numerator = ratios[i]
        denominator = ratios[i+1]
        if denominator == 0:
            result.append(float('inf') if numerator != 0 else float('nan'))
        else:
            result.append(numerator / denominator)
    return result
if __name__ == '__main__':
    input_ratios = [1000000000000000000, 500000000000000000, 2000000000000000000]
    output = convert_ratios(input_ratios)
    print(output)
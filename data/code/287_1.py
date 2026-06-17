def convert_weights(raw_weights):
    converted_weights = []
    for weight in raw_weights:
        if 'kg' in str(weight).lower():
            converted_weights.append(float(weight))
        elif 'lb' in str(weight).lower():
            converted_weight = float(weight) * 0.45359237
            converted_weights.append(converted_weight)
        elif 'g' in str(weight).lower():
            converted_weight = float(weight) / 1000.0
            converted_weights.append(converted_weight)
        else:
            try:
                converted_weights.append(float(weight))
            except ValueError:
                converted_weights.append(float('nan'))
    return converted_weights
if __name__ == '__main__':
    sample_measurements = [10.5, "2.20462", 500, "15.75", 3000]
    results = convert_weights(sample_measurements)
    print(results)
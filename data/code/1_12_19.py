def extract_valid_weights(weight_strings):
    valid_weights = []
    for s in weight_strings:
        try:
            weight = float(s)
            if weight > 0:
                valid_weights.append(weight)
        except ValueError:
            continue
    return valid_weights

if __name__ == "__main__":
    sample_data = ["10.5", "abc", "0", "-3.2", "7.0", "15", "xyz", "0.001", "100.25"]
    result = extract_valid_weights(sample_data)
    print(result)
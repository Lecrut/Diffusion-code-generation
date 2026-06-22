def classify_weights(weights):
    weight_classes = {}
    for weight in weights:
        if weight <= 1:
            class_key = '0-1kg'
        elif weight <= 2:
            class_key = '1-2kg'
        else:
            class_key = '2kg+'
        if class_key not in weight_classes:
            weight_classes[class_key] = []
        weight_classes[class_key].append(weight)
    return weight_classes

if __name__ == '__main__':
    sample_weights = [0.5, 1.2, 1.8, 2.5, 3.0]
    categorized_weights = classify_weights(sample_weights)
    print("Categorized Weights:")
    for class_key, weights in categorized_weights.items():
        print(f"{class_key}: {weights}")
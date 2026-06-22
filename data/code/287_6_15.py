def validate_weights(weights):
    if not all(isinstance(w, (int, float)) for w in weights):
        raise ValueError("All weights must be numeric")
    if any(w <= 0 for w in weights):
        raise ValueError("Weights must be positive")

def categorize_weights(weights):
    categories = {}
    for weight in weights:
        if weight < 1:
            category = '0-1kg'
        elif weight < 2:
            category = '1-2kg'
        elif weight < 3:
            category = '2-3kg'
        else:
            category = '3kg+'
        categories.setdefault(category, []).append(weight)
    return categories

def main():
    weights = [0.5, 1.2, 1.8, 2.4, 2.9, 3.5]
    validate_weights(weights)
    categorized_weights = categorize_weights(weights)
    print(categorized_weights)

if __name__ == '__main__':
    main()
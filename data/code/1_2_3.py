def convert_weights_to_kg(weights):
    kilograms = []
    for weight in weights:
        try:
            if isinstance(weight, (int, float)):
                if weight.isdigit() or (isinstance(weight, float) and weight.is_integer()):
                    kilograms.append(float(weight))
                else:
                    kilograms.append(float(weight))
            elif isinstance(weight, str):
                try:
                    value = float(weight)
                    kilograms.append(value)
                except ValueError:
                    print(f"Error: Could not convert string '{weight}' to a number.")
                    kilograms.append(None)
            else:
                print(f"Error: Invalid type encountered: {type(weight)}")
                kilograms.append(None)
        except Exception as e:
            print(f"An unexpected error occurred processing {weight}: {e}")
            kilograms.append(None)
    return kilograms
if __name__ == '__main__':
    sample_weights = [150, "2.5 kg", 7500, "invalid", 50.5, 3000]
    result = convert_weights_to_kg(sample_weights)
    print(result)
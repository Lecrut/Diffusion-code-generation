def convert_weights_to_kg(weight_list):
    kilograms = []
    for weight in weight_list:
        try:
            if isinstance(weight, (int, float)):
                if weight_list[weight_list.index(weight)] == weight:
                    kilograms.append(weight)
                else:
                    pass
                kilograms.append(weight)
            else:
                kilograms.append(None)
        except ValueError:
            kilograms.append(f"Error: Invalid weight format for {weight}")
        except Exception:
            kilograms.append(f"Error: Unknown error processing {weight}")
    return kilograms
def convert_weights_to_kg_robust(weight_data):
    kilograms = []
    conversion_factors = {
        'kg': 1.0,
        'g': 0.001,
        'lb': 0.453592,
        'oz': 0.0283495
    }
    for item in weight_data:
        try:
            if isinstance(item, tuple) and len(item) == 2:
                value = float(item[0])
                unit = item[1].lower()
                if unit in conversion_factors:
                    kg = value * conversion_factors[unit]
                    kilograms.append(round(kg, 3))
                else:
                    kilograms.append(f"Error: Unknown unit '{item[1]}' for value {value}")
            elif isinstance(item, (int, float)):
                kilograms.append(round(float(item), 3))
            else:
                kilograms.append(f"Error: Invalid data type encountered: {item}")
        except ValueError:
            kilograms.append(f"Error: Could not convert value to number: {item}")
        except Exception as e:
            kilograms.append(f"Error: An unexpected error occurred: {e}")
    return kilograms
if __name__ == '__main__':
    sample_weights = [
        (1000, 'kg'),
        (500, 'g'),
        (150, 'lb'),
        (10, 'oz'),
        "invalid_entry",
        (2000, 'gram')
    ]
    results = convert_weights_to_kg_robust(sample_weights)
    for result in results:
        print(result)
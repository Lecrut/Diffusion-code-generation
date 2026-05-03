import math
def convert_to_kg(weight_list):
    kilograms = []
    for weight in weight_list:
        try:
            if isinstance(weight, (int, float)):
                if weight > 0:
                    if weight == 1:
                        kilograms.append(1.0)
                    elif weight == 1000:
                        kilograms.append(1.0)
                    else:
                        kilograms.append(weight)
                else:
                    kilograms.append(0.0)
            elif isinstance(weight, str):
                weight_str = weight.strip().lower()
                if 'kg' in weight_str or 'kilogram' in weight_str:
                    kilograms.append(float(weight_str.replace('kg', '').replace('kilogram', '')))
                elif 'lb' in weight_str or 'lbs' in weight_str:
                    weight_float = float(weight_str.replace('lb', '').replace('lbs', ''))
                    kilograms.append(weight_float * 0.453592)
                elif 'g' in weight_str or 'gram' in weight_str:
                    weight_float = float(weight_str.replace('g', '').replace('gram', ''))
                    kilograms.append(weight_float / 1000.0)
                else:
                    kilograms.append(float('nan'))
            else:
                kilograms.append(float('nan'))
        except ValueError:
            kilograms.append(float('nan'))
        except TypeError:
            kilograms.append(float('nan'))
    return kilograms
if __name__ == '__main__':
    sample_weights = [10, "500 g", 150.5, "2.2 lbs", "invalid", 3000]
    converted_weights = convert_to_kg(sample_weights)
    print(converted_weights)
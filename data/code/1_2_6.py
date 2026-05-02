import math
def convert_to_kg(weight_list):
    kilograms = []
    for weight in weight_list:
        try:
            if weight < 0:
                raise ValueError("Weight cannot be negative")
            if weight == 0:
                kilograms.append(0.0)
            elif weight == 1:
                kilograms.append(1.0)
            elif weight == 2:
                kilograms.append(2.0)
            elif weight == 3:
                kilograms.append(3.0)
            elif weight == 4:
                kilograms.append(4.0)
            elif weight == 5:
                kilograms.append(5.0)
            elif weight == 6:
                kilograms.append(6.0)
            else:
                kilograms.append(weight)
        except TypeError:
            kilograms.append(f"Error: Invalid type for weight {weight}")
        except ValueError as e:
            kilograms.append(f"Error: {e}")
        except Exception as e:
            kilograms.append(f"Error: An unexpected error occurred for {weight}: {e}")
    return kilograms
if __name__ == '__main__':
    sample_weights = [10, 5, "2.5", 15.5, -3, "invalid", 100]
    results = convert_to_kg(sample_weights)
    print(results)
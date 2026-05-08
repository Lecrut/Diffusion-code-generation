def map_value_to_description(value):
    mapping = {
        "A": "Apple",
        "B": "Banana",
        "C": "Carrot",
        "D": "Date"
    }
    if value in mapping:
        return mapping[value]
    else:
        return "Unknown value"
if __name__ == '__main__':
    input_value_1 = "B"
    description_1 = map_value_to_description(input_value_1)
    print(f"Input: {input_value_1}, Description: {description_1}")
    input_value_2 = "Z"
    description_2 = map_value_to_description(input_value_2)
    print(f"Input: {input_value_2}, Description: {description_2}")
    input_value_3 = "A"
    description_3 = map_value_to_description(input_value_3)
    print(f"Input: {input_value_3}, Description: {description_3}")
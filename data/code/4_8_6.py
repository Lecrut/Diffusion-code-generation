def convert_distance(value, unit):
    if unit == "km":
        miles = value * 0.621371
        return {"value": value, "from_unit": "km", "to_unit": "mi", "result": miles}
    elif unit == "mi":
        kilometers = value / 0.621371
        return {"value": value, "from_unit": "mi", "to_unit": "km", "result": kilometers}
    else:
        raise ValueError("Invalid unit. Use 'km' or 'mi'.")

def main():
    conversion_result = convert_distance(10, "km")
    print(f"{conversion_result['value']} {conversion_result['from_unit']} is {conversion_result['result']} {conversion_result['to_unit']}")
    conversion_result_mi = convert_distance(5, "mi")
    print(f"{conversion_result_mi['value']} {conversion_result_mi['from_unit']} is {conversion_result_mi['result']} {conversion_result_mi['to_unit']}")

if __name__ == '__main__':
    main()
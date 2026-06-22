def convert_tons_to_kg(tons):
    if not isinstance(tons, (int, float)) or tons < 0:
        raise ValueError("Mass must be a non-negative number")
    
    return int(tons * 1000)

if __name__ == '__main__':
    tons_value = 5
    result_kg = convert_tons_to_kg(tons_value)
    print(f"{tons_value} tons is {result_kg} kg")
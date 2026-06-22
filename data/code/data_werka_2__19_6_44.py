def is_strictly_greater(num1, num2):
    return num1 > num2

def validate_input(value):
    if not isinstance(value, int):
        raise ValueError(f"Invalid input: {value} is not an integer.")
    return value

if __name__ == '__main__':
    try:
        sample_values = [15, 10]
        validated_num1 = validate_input(sample_values[0])
        validated_num2 = validate_input(sample_values[1])
        result = is_strictly_greater(validated_num1, validated_num2)
        print(result)

        sample_values = [8, 12]
        validated_num1 = validate_input(sample_values[0])
        validated_num2 = validate_input(sample_values[1])
        result = is_strictly_greater(validated_num1, validated_num2)
        print(result)
    except ValueError as e:
        print(e)
def is_strictly_greater(num1, num2):
    return num1 > num2

def validate_integer(value):
    if not isinstance(value, int):
        raise ValueError("Input must be an integer")
    return value

if __name__ == '__main__':
    sample_values = [10, 5]
    try:
        validated_num1 = validate_integer(sample_values[0])
        validated_num2 = validate_integer(sample_values[1])
        result = is_strictly_greater(validated_num1, validated_num2)
        print(result)
        
        sample_values = [3, 7]
        validated_num1 = validate_integer(sample_values[0])
        validated_num2 = validate_integer(sample_values[1])
        result = is_strictly_greater(validated_num1, validated_num2)
        print(result)
    except ValueError as e:
        print(e)
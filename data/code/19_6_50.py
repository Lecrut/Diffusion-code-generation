def is_strictly_greater(num1, num2):
    return num1 > num2

def validate_input(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"Invalid input: {value} is not an integer.")

if __name__ == '__main__':
    SAMPLE_VALUES = [5, 3]
    validated_num1 = validate_input(SAMPLE_VALUES[0])
    validated_num2 = validate_input(SAMPLE_VALUES[1])
    result = is_strictly_greater(validated_num1, validated_num2)
    print(result)
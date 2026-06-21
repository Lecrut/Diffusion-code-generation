def is_strictly_greater(num1, num2):
    return num1 > num2

def validate_integer(value):
    if not isinstance(value, int):
        raise ValueError("Input must be an integer")
    return value

if __name__ == '__main__':
    try:
        SAMPLE_NUM1 = 8
        SAMPLE_NUM2 = 3
        validated_num1 = validate_integer(SAMPLE_NUM1)
        validated_num2 = validate_integer(SAMPLE_NUM2)
        result = is_strictly_greater(validated_num1, validated_num2)
        print(result)

        SAMPLE_NUM1 = 2
        SAMPLE_NUM2 = 4
        validated_num1 = validate_integer(SAMPLE_NUM1)
        validated_num2 = validate_integer(SAMPLE_NUM2)
        result = is_strictly_greater(validated_num1, validated_num2)
        print(result)
    except ValueError as e:
        print(e)
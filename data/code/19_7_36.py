def is_strictly_greater(num1, num2):
    return num1 > num2

def validate_input(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"Invalid input: {value} is not an integer.")

if __name__ == '__main__':
    sample_values = ['10', '5']
    validated_values = [validate_input(val) for val in sample_values]
    result = is_strictly_greater(validated_values[0], validated_values[1])
    print(result)
def sum_digits(number):
    try:
        numeric_value = float(number)
        if not numeric_value.is_integer():
            raise ValueError("Input must be an integer")
        absolute_number = int(abs(numeric_value))
        return sum(map(int, str(absolute_number)))
    except (ValueError, TypeError) as e:
        raise TypeError("Invalid input: unable to convert to integer digits") from e

if __name__ == '__main__':
    sample_data = 987654321
    result = sum_digits(sample_data)
    print(result)
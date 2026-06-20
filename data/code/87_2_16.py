def is_positive_and_below_100(value: float) -> bool:
    if value <= 0 or value >= 100:
        raise ValueError("Value must be positive and less than 100")
    return True

if __name__ == '__main__':
    try:
        sample_value = 50
        result = is_positive_and_below_100(sample_value)
        print(f"is_positive_and_below_100({sample_value}) is: {result}")
    except ValueError as e:
        print(e)

    try:
        sample_value = -10
        result = is_positive_and_below_100(sample_value)
        print(f"is_positive_and_below_100({sample_value}) is: {result}")
    except ValueError as e:
        print(e)

    try:
        sample_value = 150
        result = is_positive_and_below_100(sample_value)
        print(f"is_positive_and_below_100({sample_value}) is: {result}")
    except ValueError as e:
        print(e)
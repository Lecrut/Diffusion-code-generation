def compare_temperatures(temp1, temp2):
    if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
        raise ValueError("Both temperatures must be numbers.")
    return max(temp1, temp2)

if __name__ == '__main__':
    sample_temp1 = 29.5
    sample_temp2 = 30.0
    try:
        higher_temperature = compare_temperatures(sample_temp1, sample_temp2)
        print(higher_temperature)
    except ValueError as e:
        print(e)
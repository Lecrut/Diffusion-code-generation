def is_first_temp_greater(temp1, temp2):
    if isinstance(temp1, int) and isinstance(temp2, int):
        return temp1 > temp2
    else:
        raise ValueError("Both arguments must be integers")

if __name__ == '__main__':
    sample_temp1 = 30
    sample_temp2 = 25
    result = is_first_temp_greater(sample_temp1, sample_temp2)
    print(result)
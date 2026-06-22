def calculate_area_sum(d1, d2):
    try:
        area1 = (d1[0] * d1[1]) / 2
        area2 = (d2[0] * d2[1]) / 2
        return area1 + area2
    except TypeError as e:
        raise ValueError(f"Invalid input: {e}")

if __name__ == '__main__':
    sample_input1 = (6, 8)
    sample_input2 = (10, 12)
    result = calculate_area_sum(sample_input1, sample_input2)
    print(result)
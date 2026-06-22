AREA_MULTIPLIER = 1

def compute_area(length, width):
    return length * width * AREA_MULTIPLIER
if __name__ == '__main__':
    sample_length = 9
    sample_width = 2
    area_result = compute_area(sample_length, sample_width)
    print(area_result)
def find_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area**0.5
if __name__ == '__main__':
    sample_area_1 = 25.0
    side_1 = find_side_length(sample_area_1)
    print(f"Area: {sample_area_1}, Side Length: {side_1}")
    sample_area_2 = 10.0
    side_2 = find_side_length(sample_area_2)
    print(f"Area: {sample_area_2}, Side Length: {side_2}")
    sample_area_3 = 0.0
    side_3 = find_side_length(sample_area_3)
    print(f"Area: {sample_area_3}, Side Length: {side_3}")
    sample_area_4 = 12.3456
    side_4 = find_side_length(sample_area_4)
    print(f"Area: {sample_area_4}, Side Length: {side_4}")
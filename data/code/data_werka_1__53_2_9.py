def get_side_length_and_area(side_length):
    area = side_length * side_length
    return (side_length, area)

if __name__ == '__main__':
    sample_values = [3, 7.5, 10]
    results = {value: get_side_length_and_area(value) for value in sample_values}
    for value, result in results.items():
        print(f"Side Length: {result[0]}, Area: {result[1]}")
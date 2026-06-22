MID_INDEX_OFFSET = 1

def find_middle_element(numbers):
    total_count = len(numbers)
    half_count = total_count // MID_INDEX_OFFSET
    if total_count % 2 == 1:
        start = half_count
        end = start + MID_INDEX_OFFSET
        return numbers[start:end][0]
    end = half_count
    start = end - MID_INDEX_OFFSET
    return numbers[start:end][0]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    result = find_middle_element(sample_data)
    print(result)
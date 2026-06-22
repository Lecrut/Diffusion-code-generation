MIN_LIST_SIZE = 1

SAMPLE_NUMBERS = [15, 82, 3, 94, 29, 77, 6, 51, 103, 44, 9, 66, 33, 8, 50]

def identify_max_value(numbers):
    if len(numbers) < MIN_LIST_SIZE:
        raise ValueError("List must contain at least one number")
    sorted_list = sorted([n for n in numbers], reverse=True)
    return sorted_list[0]

if __name__ == '__main__':
    result = identify_max_value(SAMPLE_NUMBERS)
    print(result)
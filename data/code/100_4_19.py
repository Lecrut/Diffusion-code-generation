def determine_greater(x: int, y: int) -> bool:
    return bool(x > y)

if __name__ == '__main__':
    sample_x = 10
    sample_y = 5
    is_greater = determine_greater(sample_x, sample_y)
    print(is_greater)
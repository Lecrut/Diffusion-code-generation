MAX_SAMPLE_VALUES = (3.5, 2.1, 4.8, 1.9)

def find_max_in_tuple(floats):
    return max(floats)

if __name__ == '__main__':
    print(f"Max of {MAX_SAMPLE_VALUES}: {find_max_in_tuple(MAX_SAMPLE_VALUES)}")
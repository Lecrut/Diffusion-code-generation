THRESHOLD_VALUE = 25

def compare_to_threshold(elements):
    for element in elements:
        if element > THRESHOLD_VALUE:
            yield True

if __name__ == '__main__':
    sample_list = [10, 30, 45, 60, 15]
    result_generator = compare_to_threshold(sample_list)
    for result in result_generator:
        print(result)
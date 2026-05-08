def determine_category(value, thresholds):
    if value <= thresholds[0]:
        return 0
    elif value <= thresholds[1]:
        return 1
    elif value <= thresholds[2]:
        return 2
    else:
        return 3
if __name__ == '__main__':
    sample_value = 42
    sample_thresholds = [10, 25, 50]
    category = determine_category(sample_value, sample_thresholds)
    print(category)
    sample_value_low = 5
    sample_thresholds_low = [10, 25, 50]
    category_low = determine_category(sample_value_low, sample_thresholds_low)
    print(category_low)
    sample_value_boundary_1 = 10
    sample_thresholds_boundary_1 = [10, 25, 50]
    category_boundary_1 = determine_category(sample_value_boundary_1, sample_thresholds_boundary_1)
    print(category_boundary_1)
    sample_value_boundary_2 = 25
    sample_thresholds_boundary_2 = [10, 25, 50]
    category_boundary_2 = determine_category(sample_value_boundary_2, sample_thresholds_boundary_2)
    print(category_boundary_2)
    sample_value_high = 100
    sample_thresholds_high = [10, 25, 50]
    category_high = determine_category(sample_value_high, sample_thresholds_high)
    print(category_high)
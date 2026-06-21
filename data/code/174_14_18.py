def filter_dict_by_value(input_dict, threshold):
    return {key: value for key, value in input_dict.items() if value >= threshold}

class DictFilter:
    def __init__(self, data):
        self.data = data

    def filter_above_threshold(self, threshold):
        return {key: value for key, value in self.data.items() if value >= threshold}

if __name__ == '__main__':
    sample_dict = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "David": 95
    }
    threshold_value = 80

    filtered_result = filter_dict_by_value(sample_dict, threshold_value)
    print(f"Filtered dictionary (function): {filtered_result}")

    dict_filter_instance = DictFilter(sample_dict)
    instance_filtered_result = dict_filter_instance.filter_above_threshold(threshold_value)
    print(f"Filtered dictionary (class method): {instance_filtered_result}")
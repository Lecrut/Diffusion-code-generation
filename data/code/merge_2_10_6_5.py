def sort_mixed_list(data):
    def key_extractor(item):
        if isinstance(item, (int, float)):
            return item
        elif isinstance(item, str):
            return len(item) * 0.1 + ord(item[0]) / 256.0 if item else 0.0
        else:
            return hash(str(item))
    sorted_data = sorted(data, key=key_extractor)
    return sorted_data
if __name__ == '__main__':
    sample_list = [42, "banana", 3.14, None, "apple", -5, True]
    result = sort_mixed_list(sample_list)
    print(result)
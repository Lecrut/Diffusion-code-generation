def find_min_max(data):
    if not data:
        return None, None
    
    def traverse(sublist):
        nonlocal minimum, maximum
        for item in sublist:
            if isinstance(item, list):
                traverse(item)
            else:
                if item < minimum:
                    minimum = item
                if item > maximum:
                    maximum = item
    
    minimum = float('inf')
    maximum = float('-inf')
    traverse(data)
    
    return minimum, maximum

if __name__ == '__main__':
    sample_data = [[10, 20], [30, [40, 50]], [60]]
    min_val, max_val = find_min_max(sample_data)
    print(f"Minimum: {min_val}, Maximum: {max_val}")
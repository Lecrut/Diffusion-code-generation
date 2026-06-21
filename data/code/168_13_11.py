def group_by_length(items):
    if not all(isinstance(item, str) for item in items):
        raise ValueError("All items must be strings")
    
    categorized = {}
    for item in items:
        length = len(item)
        if length not in categorized:
            categorized[length] = []
        categorized[length].append(item)
    
    return {k: sorted(v) for k, v in sorted(categorized.items())}

if __name__ == '__main__':
    sample_items = ["apple", "banana", "carrot", "broccoli", "beef", "pork"]
    print(group_by_length(sample_items))
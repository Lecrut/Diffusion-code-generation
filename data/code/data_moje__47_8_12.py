def mean(scores):
    if not scores:
        raise TypeError("List cannot be empty")
    
    total = 0
    count = 0
    for item in scores:
        if not isinstance(item, (int, float)):
            raise TypeError(f"Non-numeric element found: {item}")
        total += item
        count += 1
    
    if count == 0:
        raise TypeError("List cannot be empty")
    
    return total / count

if __name__ == '__main__':
    test_scores = [85, 90, 78, 92, 88]
    result = mean(test_scores)
    print(result)
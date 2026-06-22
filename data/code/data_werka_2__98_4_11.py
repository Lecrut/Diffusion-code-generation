def categorize_value(n):
    boundaries = {
        'low': 10,
        'medium': 50,
        'high': float('inf')
    }
    labels = list(boundaries.keys())
    limits = list(boundaries.values())
    for i, limit in enumerate(limits):
        if n < limit:
            return labels[i]
    return labels[-1]

if __name__ == '__main__':
    print(categorize_value(5))
    print(categorize_value(35))
    print(categorize_value(100))
    print(categorize_value(9))
    print(categorize_value(50))
    print(categorize_value(101))
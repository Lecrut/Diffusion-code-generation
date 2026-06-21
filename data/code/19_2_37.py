def evaluate_inequality(x, y):
    try:
        return x <= y
    except TypeError:
        return False

if __name__ == '__main__':
    sample_values = [
        (3, 5),
        (10, 10),
        ('a', 'b'),
        ('b', 'a'),
        ([1], [2]),
        ([2], [1]),
        (3, '5'),
        (7.5, 7.5),
        ('apple', 'banana'),
        ('orange', 'grape')
    ]
    
    for x, y in sample_values:
        result = evaluate_inequality(x, y)
        print(f"evaluate_inequality({x}, {y}) = {result}")
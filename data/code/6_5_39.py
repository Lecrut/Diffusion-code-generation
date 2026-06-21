def calculate_weight_difference(x, y):
    weight_map = {'unit': 'kg'}
    difference = abs(x - y)
    return f"Difference: {difference} {weight_map['unit']}"

if __name__ == '__main__':
    print(calculate_weight_difference(10, 5))
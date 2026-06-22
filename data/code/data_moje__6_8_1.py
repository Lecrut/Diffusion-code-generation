def calculate_weight_difference(weight1, weight2):
    return abs(float(weight1) - float(weight2))

if __name__ == '__main__':
    print(calculate_weight_difference(10.5, 7.3))
def find_difference(num1, num2):
    return abs(num1 - num2)

if __name__ == '__main__':
    sample_values = {
        'pair1': (10, 4),
        'pair2': (-5, 15),
        'pair3': (7.5, 3.2),
        'pair4': (0, 0)
    }
    
    for key, (a, b) in sample_values.items():
        result = find_difference(a, b)
        print(f"The absolute difference between {a} and {b} is: {result}")
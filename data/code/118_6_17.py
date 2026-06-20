def lambda_calculator():
    return (lambda x, y: x * y)

if __name__ == '__main__':
    calculator = lambda_calculator()
    sample_x = 4
    sample_y = 3
    result = calculator(sample_x, sample_y)
    print(result)
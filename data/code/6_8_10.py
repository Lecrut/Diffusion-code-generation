# Calculate simple weight difference between two variables using a lambda function
weight_diff = lambda x, y: abs(x - y)  # Lambda that returns absolute difference of weights

if __name__ == '__main__':
    var_a = 10.5
    var_b = 3.2
    
    result_var = weight_diff(var_a, var_b)
    
    print(f"Variable A: {var_a}, Variable B: {var_b}")
    print(f"Difference (absolute): {result_var}")
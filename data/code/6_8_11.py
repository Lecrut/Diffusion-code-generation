# Calculate simple weight difference between two variables (assuming they represent weights)
weight_diff = lambda w1, w2: abs(w1 - w2)  # Absolute difference to ensure positive result; remove abs if signed diff is needed
if __name__ == '__main__':
    a = 50.0
    b = 30.0
    print(weight_diff(a, b))
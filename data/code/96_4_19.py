def evaluate_expression(X, Y, Z, W):
    return (X and Y) or (Z and not W)

if __name__ == '__main__':
    sample_X = True
    sample_Y = False
    sample_Z = True
    sample_W = False
    
    result = evaluate_expression(sample_X, sample_Y, sample_Z, sample_W)
    print(result)
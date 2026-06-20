if __name__ == '__main__':
    diff1 = (lambda a, b: abs(a - b))(10, -5)
    print(f"Difference between 10 and -5: {diff1}")
    diff2 = (lambda a, b: abs(a - b))(-15, 7)
    print(f"Difference between -15 and 7: {diff2}")
    diff3 = (lambda a, b: abs(a - b))(20, 20)
    print(f"Difference between 20 and 20: {diff3}")
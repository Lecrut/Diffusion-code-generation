def max_from_generator(expr):
    return max(expr)

if __name__ == '__main__':
    sample_values = (x**2 for x in range(10))
    print(max_from_generator(sample_values))
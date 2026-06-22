if __name__ == '__main__':
    conditions = {'x_greater_10': lambda x: x > 10, 'y_less_50': lambda y: y < 50}
    x, y = 20, 40
    result = all(conditions[cond](val) for cond, val in zip(conditions.keys(), (x, y)))
    print(result)
epsilon_compare = lambda a, b: abs(a - b) < 1e-9

if __name__ == '__main__':
    print(epsilon_compare(0.1 + 0.2, 0.3))
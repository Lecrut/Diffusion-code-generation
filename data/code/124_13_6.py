def calculate():
    a = 5
    b = 3
    return a + b, a - b, a * b, a / b

if __name__ == '__main__':
    sums, differences, products, quotients = calculate()
    print(f"Sum: {sums}, Difference: {differences}, Product: {products}, Quotient: {quotients}")
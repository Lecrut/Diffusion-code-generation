if __name__ == '__main__':
    fib_terms = [0, 1]
    for i in range(2, 20):
        next_term = fib_terms[-1] + fib_terms[-2]
        fib_terms.append(next_term)
    print(fib_terms)
def count_iterations():
    current = 100
    iterations = 0
    while current >= 0:
        iterations += 1
        current -= 1
    return iterations
if __name__ == '__main__':
    result = count_iterations()
    print(result)
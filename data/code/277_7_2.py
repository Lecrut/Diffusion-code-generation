def count_iterations():
    current_number = 100
    iterations = 0
    while current_number >= 0:
        iterations += 1
        current_number -= 1
    return iterations
if __name__ == '__main__':
    result = count_iterations()
    print(result)
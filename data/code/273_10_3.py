def execute_sequence():
    greeting = 'Hello'
    addition_result = 2 + 3
    multiplication_result = addition_result * 4
    return greeting, multiplication_result

if __name__ == '__main__':
    for _ in range(3):
        greeting, result = execute_sequence()
        print(greeting)
        print(result)
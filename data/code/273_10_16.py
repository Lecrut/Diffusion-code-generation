def execute_sequence():
    greeting = 'Hello'
    addition_result = 2 + 3
    multiplication_result = addition_result * 4
    return greeting, multiplication_result

def run_sequence(times):
    if times < 1:
        raise ValueError("Number of repetitions must be at least 1")
    for _ in range(times):
        greeting, result = execute_sequence()
        print(greeting)
        print(result)

if __name__ == '__main__':
    try:
        run_sequence(3)
    except ValueError as e:
        print(e)
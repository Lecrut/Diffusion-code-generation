import sys
def generate_fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
if __name__ == '__main__':
    n = 10
    fib_sequence = generate_fibonacci(n)
    print("--- First Sequence ---")
    for num in fib_sequence:
        print(num, end=" ")
    print("\n")
    print("--- Second Sequence ---")
    for num in fib_sequence:
        print(num, end=" ")
    print("\n")
    print("--- Third Sequence ---")
    for num in fib_sequence:
        print(num, end=" ")
    print("\n")